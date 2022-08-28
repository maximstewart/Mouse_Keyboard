# Python imports

# Lib imports
from gi.repository import GObject


# Application imports
from .widgets.key import Key




class SignalsMixin:
    """docstring for SignalsMixin."""

    def setup_custom_event_signals(self):
        GObject.signal_new('toggle-caps', Key, GObject.SIGNAL_RUN_LAST, GObject.TYPE_PYOBJECT, (GObject.TYPE_PYOBJECT,))
        GObject.signal_new('toggle-symbol-keys', Key, GObject.SIGNAL_RUN_LAST, GObject.TYPE_PYOBJECT, (GObject.TYPE_PYOBJECT,))
