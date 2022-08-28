# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .widgets.defined_keys import Esc_Key, AT_Key, Space_Key, COM_Key




class Bottom_Key_Row(Gtk.Box):
    def __init__(self):
        super(Bottom_Key_Row, self).__init__()

        self.set_property("homogeneous", True)

        for key in [Esc_Key(), Space_Key(), AT_Key(), COM_Key()]:
            self.add(key)
