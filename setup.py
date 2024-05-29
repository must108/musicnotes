from setuptools import setup

with open('README.md', encoding = 'utf-8') as f:
    long_description = f.read()

setup (
    name = 'musicnotes',
    version = '1.11',
    description = 'Play music notes in your Python scripts with ease.',
    long_description = long_description,
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',   
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
    ],
    packages = ['musicnotes'],
    package_data = {
        'musicnotes': ['assets/piano/*.mp3', 'assets/guitar/*.mp3'],
    },
)