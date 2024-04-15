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