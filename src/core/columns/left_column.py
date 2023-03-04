# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.defined_keys import Esc_Key
from ..widgets.defined_keys import Tab_Key
from ..widgets.defined_keys import CAPS_Key




class Left_Column(Gtk.Box):
    """docstring for Left_Column."""

    def __init__(self):
        super(Left_Column, self).__init__()

        self.setup_styling()

        for key in [Tab_Key(), Esc_Key(), CAPS_Key()]:
            self.add(key)

        self.show_all()

    def setup_styling(self):
        self.set_orientation(1) # HORIZONTAL = 0, VERTICAL = 1
