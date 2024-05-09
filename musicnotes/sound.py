'''
For playing sounds on various systems
'''

import logging
log = logging.getLogger(__name__)

import sys
from sys import argv
from time import sleep
from inspect import getsourcefile
from subprocess import check_call
from threading import Thread
from threading import Timer
from platform import system 
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

# windows
from ctypes import create_unicode_buffer, wintypes
try:
    from ctypes import windll
except ImportError:
    pass
from os import getcwd
from os.path import abspath, exists

# macos
try:
    from Foundation import NSURL
except ImportError:
    pass

# linux
try:
    import gi 
    from gi.repository import Gst
except ImportError:
    pass

# python2
try:
    from urllib.request import pathname2url
except ImportError:
    from urllib import pathname2url

"""
this code is heavily inspired by 'playsound' by Taylor S. Marks, with some minor tweaks here and there:
https://github.com/TaylorSMarks/playsound

i wouldn't have learned how to use some of these modules without seeing his code.
"""

class soundException(Exception):
    pass

# takes in a file path and converts to string on python3
# returns path if on python2.
def canonicalizeFilePath(path): 
    if sys.version_info[0] >= 3:
        return str(path)
    else:
        return path
    
def OSXPath(sound, block = True):
    sound = canonicalizeFilePath(sound)

    if('://' not in sound): 
        if not sound.startswith('/'):
            sound = getcwd() + '/' + sound
        sound = 'file://' + sound

    try:
        sound.encode('ascii')
        return sound.replace(' ', '%20')
    except UnicodeEncodeError:
        parts = sound.split('://', 1)
        return parts[0] + '://' + quote(parts[1].encode('utf-8')).replace(' ', '%20')
            
    
def windowsSound(sound, block = True):
    sound = '"' + canonicalizeFilePath(sound) + '"'
    windll.winmm.mciSendStringW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.UINT, wintypes.HANDLE]
    windll.winmm.mciGetErrorStringW.argtypes = [wintypes.DWORD, wintypes.LPWSTR, wintypes.UINT]

    def windowsCommand(*command):
        buffer = create_unicode_buffer(600)
        command = ' '.join(command)
        error = int(windll.winmm.mciSendStringW(command, buffer, 599, 0))
        if error:
            errorBuff = create_unicode_buffer(600)
            windll.winmm.mciGetErrorStringW(error, errorBuff, 599)
            exceptMessage = ('\nError:' + str(error) + ' due to command:\n' + command + '\n ' + errorBuff.value)
            log.error(exceptMessage)
            raise soundException(exceptMessage)
        return buffer.value
    
    try:
        log.debug('Starting')
        windowsCommand(u'open {}'.format(sound))
        if block:
            windowsCommand(u'play {}{}'.format(sound, ' wait'))
        else:
            Thread(target = windowsCommand, args=(u'play {}{}'.format(sound, ''),)).start()
        log.debug('Returning')
    finally:
        try:
            windowsCommand(u'close {}'.format(sound))
        except soundException:
            log.warning(u'Failed to close the file: {}'.format(sound))
            pass

def macSound(sound, block = True):
    try:
        from AppKit import NSSound
    except ImportError:
        log.warning("could not find a copy of AppKit. macOS's system copy will be used.")
        sys.path.append('System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC')
        from AppKit import NSSound

    sound = OSXPath(sound)
    url = NSURL.URLWithString_(sound)
    if not url:
        raise soundException(u'Cannot find a sound with filename: {}'.format(sound))
    
    for i in range(5):
        nssound = NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
        if nssound:
            break
        else:
            log.debug(u'Failed to load sound with a good URL: {}'.format(sound))
        nssound.play()

        if block:
            sleep(nssound.duration())

def nixSound(sound, block = True):
    sound = canonicalizeFilePath(sound)
    gi.require_version('Gst', '1.0')
    from gi.repository import Gst

    Gst.init(None)

    playbin = Gst.ElementFactory.make('playbin', 'playbin')
    if sound.startswith(('http://', 'https://')):
        playbin.props.uri = sound
    else:
        path = abspath(sound)
        if not exists(path):
            raise soundException(u'File not found: {}'.format(path))
        playbin.props.uri = 'file://' + pathname2url(path)

        set_res = playbin.set_state(Gst.State.PLAYING)
        if set_res != Gst.StateChangeReturn.ASYNC:
            raise soundException("playbin.set_state returned " + repr(set_res))

        log.debug('Playing...')
        if block:
            bus = playbin.get_bus()
            try:
                bus.poll(Gst.MessageType.EOS, Gst.CLOCK_TIME_NONE)
            finally:
                playbin.set_state(Gst.State.NULL)
        else:
            Thread(target = lambda: bus.poll(Gst.MessageType.EOS, Gst.CLOCK_TIME_NONE)).start()

        log.debug('Playing finished.')

def anotherPython(otherPython, sound, block = True, macOS = False):
    sound = canonicalizeFilePath(sound)

    class PropogatingThread(Thread):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.exc = None
            self.ret = FileNotFoundError

        def run(self):
            try:
                self.ret = self._target(*self._args, **self._kwargs)
            except BaseException as e:
                self.exc = e
        
        def join(self, timeout = None):
            super().join(timeout)
            if self.exc:
                raise self.exc
            return self.ret
        
    if not exists(abspath(sound)):
        raise soundException(u'Cannot find a sound with filename: {}'.format(sound))
    
    soundPath = abspath(getsourcefile(lambda: 0))
    t = PropogatingThread(target = lambda: check_call([otherPython, 
                                                       soundPath, OSXPath(sound) if macOS else sound]))
    t.start()
    if block:
        t.join()

system = system()

if system == 'Windows':
    soundPlayer = windowsSound
elif system == 'Darwin':
    soundPlayer = macSound
    if sys.version_info[0] > 2:
        try:
            from AppKit import NSSound
        except ImportError:
            log.warning("this library is current running on a python 2 subprocess. run 'pip install PyObjC' for better results.")
            soundPlayer = lambda sound, block = True: anotherPython(
                '/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python', 
                                                            sound, block, macOS = True)
else:
    soundPlayer = nixSound
    if __name__ != '__main__': # prevent infinite recursion
        try:
            gi.require_version('Gst', '1.0')
        except:
            log.warning("this library is running on another python subprocess. run 'pip install pygobject for better results.")
            soundPlayer = lambda sound, block = True: anotherPython(
                '/usr/bin/python3', sound, block, macOS = False)

del system

if __name__ == '__main__':
    soundPlayer(argv[1])
