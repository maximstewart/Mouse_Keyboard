# Python imports
import os
import builtins
import threading

# Lib imports

# Application imports
from libs.pyautogui_control import ControlMixin
from libs.endpoint_registry import EndpointRegistry
from libs.event_system import EventSystem



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



class MissingConfigError(Exception):
    pass


class Pyautogui_Controller(ControlMixin):
    def __init__(self):
        self.isCtrlOn       = False
        self.isShiftOn      = False
        self.isAltOn        = False




keys_json = {
    "keys": {
        "row1": {
            "pKeys": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            "sKeys": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        },
        "row2": {
            "pKeys": ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            "sKeys": ['\\', '^', '#', '$', '%', '&', '-', '_', '"', '*']
        },
        "row3": {
            "pKeys": ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', "'"],
            "sKeys": ['/', '|', ':', '=', '+', '', '', '', ';', '!']
        },
        "row4": {
            "pKeys": ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?'],
            "sKeys": ['', '', '<', '>', '[', ']', '(', ')', '{', '}']
        },
    }
}



# NOTE: Just reminding myself we can add to builtins two different ways...
# __builtins__.update({"event_system": Builtins()})
builtins.app_name          = "Mouse-Keyboard"
builtins.threaded          = threaded_wrapper
builtins.daemon_threaded   = daemon_threaded_wrapper
builtins.keys_set          = keys_json
builtins.trace_debug       = False
builtins.debug             = False
builtins.app_settings      = None
builtins.get_clipboard     = ['xclip','-selection', 'clipboard', '-o']
builtins.set_clipboard     = ['xclip','-selection','clipboard']
builtins.endpoint_registry = EndpointRegistry()
builtins.event_system      = EventSystem()
builtins.typwriter         = Pyautogui_Controller()



_USER_HOME   = os.path.expanduser('~')
_USR_PATH    = f"/usr/share/{app_name.lower()}"
_CONFIG_PATH = f"{_USER_HOME}/.config/{app_name.lower()}"
_ICON_FILE   = f"{_CONFIG_PATH}/icons/{app_name.lower()}.png"
_CSS_FILE    = f"{_CONFIG_PATH}/stylesheet.css"
_EMOJI_FILE  = f"{_CONFIG_PATH}/emoji.json"


if not os.path.exists(_ICON_FILE):
    _ICON_FILE = f"{_USR_PATH}/icons/{app_name.lower()}.png"
    if not os.path.exists(_ICON_FILE):
        print(_ICON_FILE)
        raise MissingConfigError("Unable to find the application icon.")

if not os.path.exists(_CSS_FILE):
    _CSS_FILE = f"{_USR_PATH}/stylesheet.css"
    if not os.path.exists(_CSS_FILE):
        raise MissingConfigError("Unable to find the stylesheet.")

if not os.path.exists(_EMOJI_FILE):
    _EMOJI_FILE = f"{_USR_PATH}/emoji.json"
    if not os.path.exists(_EMOJI_FILE):
        raise MissingConfigError("Unable to find the stylesheet.")



builtins.CONFIG_PATH = _CONFIG_PATH
builtins.ICON_FILE   = _ICON_FILE
builtins.CSS_FILE    = _CSS_FILE
builtins.EMOJI_FILE  = _EMOJI_FILE
