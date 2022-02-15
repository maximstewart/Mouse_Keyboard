# Python imports
import inspect


# Gtk imports


# Application imports
from utils.settings import Settings
from signal_classes.signals import Signals
from __builtins__ import Builtins


class Main(Builtins):
    def __init__(self, args):
        settings = Settings()
        builder  = settings.returnBuilder()

        # Gets the methods from the classes and sets to handler.
        # Then, builder connects to any signals it needs.
        classes  = [Signals(settings)]

        handlers = {}
        for c in classes:
            methods = None
            try:
                methods = inspect.getmembers(c, predicate=inspect.ismethod)
                handlers.update(methods)
            except Exception as e:
                pass

        builder.connect_signals(handlers)
        window = settings.createWindow()
        window.show()
