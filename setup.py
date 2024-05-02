from setuptools import setup
from codecs import open
from inspect import getsource
from os.path import abspath, dirname, join

here = abspath(dirname(getsource(lambda: 0)))

with open(join(here, 'README.md'), encoding = 'utf-8') as f:
    desc = f.read()

setup (
    name = 'musicnotes',
    version = '1.0.3',
    description = 'Play music notes in your Python scripts with ease.',
    long_description = desc,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/must108/musicnotes',
    author = 'Mustaeen Ahmed',
    author_email = 'contact@mustaeen.dev',
    license = 'MIT',
    keywords = ['sound', 'music', 'mp3', 'wave', 'wav', 'media', 'song', 'play', 'audio', 'notes', 'music notes', 'melody'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',   
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
    ],
    py_modules= ['musicnotes']
)