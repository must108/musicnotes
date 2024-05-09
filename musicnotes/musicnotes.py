from .sound import soundPlayer
import pkg_resources

def note(note, pitch = 'mid', sharp = False, flat = False, instrument = 'piano'):
    note.upper()
    if sharp and flat:
        raise Exception("A note cannot be both sharp and flat!")
    
    if pitch != 'low' and pitch != 'mid' and pitch != 'high':
        raise Exception("Not a valid pitch!")

    if ord(note) not in range(65, 72):
        raise Exception("Note is not valid!")
    
    if instrument != 'piano' and instrument != 'guitar':
        raise Exception("Instrument is not valid!")

    if sharp:
        play(note, pitch, '#', instrument)
    elif flat:
        if note == 'A': # to prevent it trying to play another symbol
            note = 'G'
        else:
            note = chr(ord(note) - 1)
                
        play(note, pitch, '#', instrument)
    else:
        play(note, pitch, '', instrument)
            
def play(note, pitch, sym = '', instrument = 'piano'): # for drier code
    if pitch == 'low':
        fp = pkg_resources.resource_filename('musicnotes', 'assets/' 
                                             + instrument + '/low' + note + sym + instrument + '.mp3')
        soundPlayer(fp, block = True)
    elif pitch == 'mid':
        fp = pkg_resources.resource_filename('musicnotes', 'assets/' 
                                             + instrument + '/mid' + note + sym + instrument + '.mp3')
        soundPlayer(fp, block = True)
    elif pitch == 'high':
        fp = pkg_resources.resource_filename('musicnotes', 'assets/' 
                                             + instrument + '/high' + note + sym + instrument + '.mp3')
        soundPlayer(fp, block = True)