# Python imports
import builtins, threading

# Lib imports

# Application imports
from utils.pyautogui_control import ControlMixin




# NOTE: Threads WILL NOT die with parent's destruction.
def threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=False).start()
    return wrapper

# NOTE: Threads WILL die with parent's destruction.
def daemon_threaded_wrapper(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper




class EndpointRegistry():
    def __init__(self):
        self._endpoints = {}

    def register(self, rule, **options):
        def decorator(f):
            self._endpoints[rule] = f
            return f

        return decorator

    def get_endpoints(self):
        return self._endpoints


class Pyautogui_Controller(ControlMixin):
    def __init__(self):
        self.isCtrlOn       = False
        self.isShiftOn      = False
        self.isAltOn        = False




keys_json = {
    "keys": {
        "row1": {
            "pKeys": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            "sKeys": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        },
        "row2": {
            "pKeys": ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            "sKeys": ['\\', '^', '#', '$', '%', '&', '-', '_', '<', '>'],
        },
        "row3": {
            "pKeys": ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', "'"],
            "sKeys": ['\\', '/', '|', ':', '=', '+', '"', '*', ';', '!'],
        },
        "row4": {
            "pKeys": ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?'],
            "sKeys": ['`', '', '', '', '[', ']', '(', ')', '{', '}']
        },
    }
}




# NOTE: Just reminding myself we can add to builtins two different ways...
# __builtins__.update({"event_system": Builtins()})
builtins.app_name          = "Mouse Keyboard"
builtins.endpoint_registry = EndpointRegistry()
builtins.typwriter         = Pyautogui_Controller()
builtins.threaded          = threaded_wrapper
builtins.daemon_threaded   = daemon_threaded_wrapper
builtins.keys_set          = keys_json
builtins.trace_debug       = False
builtins.debug             = False
builtins.app_settings      = None
