# Python imports
import signal
import os

# Lib imports

# Application imports
from libs.debugging import debug_signal_handler
from core.window import Window



class AppLaunchException(Exception):
    ...



class Application:
    """ docstring for Application. """

    def __init__(self, args, unknownargs):
        super(Application, self).__init__()

        self.setup_debug_hook()
        Window(args, unknownargs).main()


    def setup_debug_hook(self):
        try:
            # kill -SIGUSR2 <pid> from Linux/Unix or SIGBREAK signal from Windows
            signal.signal(
                vars(signal).get("SIGBREAK") or vars(signal).get("SIGUSR1"),
                debug_signal_handler
            )
        except ValueError:
            # Typically: ValueError: signal only works in main thread
            ...