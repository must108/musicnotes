from sound import soundPlayer

def note(note, pitch = 'mid', sharp = False, flat = False, instrument = 'piano'):
    note.upper()
    if sharp and flat:
        raise Exception("A note cannot be both sharp and flat!")
    
    if pitch != 'low' and pitch != 'mid' and pitch != 'high':
        raise Exception("Not a valid pitch!")

    if ord(note) not in range(65, 72):
        raise Exception("Note is not valid!")

    if instrument == 'piano':
        if sharp:
            play(note, pitch, '#')
        elif flat:
            if note == 'A': # to prevent it trying to play another symbol
                note = 'G'
            else:
                note = chr(ord(note) - 1)
                
            play(note, pitch, '#')
        else:
            play(note, pitch)
            
def play(note, pitch, sym = ''): # for drier code
    if pitch == 'low':
        soundPlayer('./assets/piano/' + 'low' + note + sym + 'piano.mp3', block = True)
    elif pitch == 'mid':
        soundPlayer('./assets/piano/' + 'mid' + note + sym + 'piano.mp3', block = True)
    elif pitch == 'high':
        soundPlayer('./assets/piano/' + 'high' + note + sym + 'piano.mp3', block = True)