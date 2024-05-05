# musicnotes

*Play music notes in your Python scripts with ease.*

# Installation

Install with pip:

```
pip install musicnotes
```

You can also install manually from the GitHub repository linked [here](https://github.com/must108/musicnotes).

# Issues

Anyone wishing to contribute to this project can focus on the following issues.

### Instruments
We need to add more instruments, and more keys to the piano, as well as more notes to the guitar as well. This would be a good first PR for anyone willing to contribute to this project.

### Asynchronous Audio
The current solution I've developed for playing the notes has trouble playing them more smoothly, and anyone who tests this software will notice how the notes sound when trying to play a song. 

### Sound Quality
Anyone with access to higher quality sounds for notes can contribute to this project by adding these sounds. Please be sure that these sounds do not violate anyone else's copyright.

### General
If you find a bug while using this software, feel free to create an issue on this repository. More on how to create an issue [here](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues).

# Documentation

Currently, this project only supports a limited number of piano keys, and up to the 5th fret on an acoustic guitar. This project is open-source, so anyone who wants to add more instruments, more keys, or higher quality audio can make a pull request and do so. You can learn more about pull requests [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

This module contains one function, "note". This function contains several arguments in order to clearly define the sound of the note. 

```python
note(note, pitch, sharp, flat, instrument)
```

## Arguments:

`note`: Takes in a letter, from A-G, and plays the corresponding note.

`pitch`: Currently, three 'pitches' are supported. `low`, `mid`, and `high`. This is due to the fact that the only instrument supported is a 36-key piano, as well as about 36 notes on a guitar. Set to `mid` by default.

`sharp`: Set to `False` by default. Set to `True` if you want to sharp the note. Remember that B# and E# do not exist.

`flat`: Set to `False` by default. Set to `True` if you want to flat the note.

`instrument`: Set to `piano` by default. Currently only supports `piano` and `guitar`, with plans to add more instruments in the future.


## soundPlayer

This portion of the project is heavily inspired by Taylor S. Marks' project, [playsound](https://github.com/TaylorSMarks/playsound). 

The main thing any contributors need to focus on is the `block` argument in `soundPlayer`. This is set to `true` by default. However, setting this to `False` will allow sounds to run asynchronously. This will be something that needs to be updated later on, as currently, the notes play very separately, and make it difficult to play smooth-flowing music.

You can also contribute by updating `soundPlayer`, possibly making it better for our use case. 

# Copyright

This software is Copyright (c) 2024 Mustaeen Ahmed 

See LICENSE for more information.
