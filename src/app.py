# Python imports
import inspect


# Gtk imports


# Application imports
from __builtins__ import *
from core.window import Window




class Application(object):
    def __init__(self, args, unknownargs):
        try:
            Window(args, unknownargs)
        except Exception as e:
            raise
