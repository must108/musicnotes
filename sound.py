"""
this code is heavily inspired by 'playsound' by Taylor S. Marks, with some minor tweaks here and there:
https://github.com/TaylorSMarks/playsound

i wouldn't have learned how to use some of these modules without seeing this code.
"""

import logging
import sys
from time import sleep
from inspect import getsourcefile
from subprocess import check_call
from threading import Thread
from platform import system 

# windows
from ctypes import create_unicode_buffer, windll, wintypes
from os import getcwd
from urllib.parse import quote
from os.path import abspath, exists
from urllib.request import pathname2url

# linux
import gi 
from gi.repository import Gst

# mac os
from AppKit import NSSound
from Foundation import NSURL

# python2
from urllib import quote
from urllib import pathname2url

log = logging.getLogger(__name__)

class soundException(exception):
    pass

"""
takes in a file path and converts to string on python3.
returns path if on python2.
"""
def canonicalizeFilePath(path): 
    if sys.version_info[0] >= 3:
        return str(path)
    else:
        return path
    
def windowsSound(sound, block = True):
    sound = '"' + canonicalizeFilePath(sound) + '"'
    windll.mciSendStringW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.UNIT, wintypes.HANDLE]
    windll.winmm.mciGetErrorStringW.argtypes = [wintypes.DWORD, wintypes.LPWSTR, wintypes.UNIT]

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

