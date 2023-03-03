# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.defined_keys import Emoji_Keys
from ..widgets.defined_keys import Backspace_Key
from ..widgets.defined_keys import Enter_Key



class Right_Column(Gtk.Box):
    """docstring for Right_Column."""

    def __init__(self):
        super(Right_Column, self).__init__()

        self.setup_styling()

        for key in [Emoji_Keys(), Backspace_Key(), Enter_Key()]:
            self.add(key)

        self.show_all()

    def setup_styling(self):
        self.set_orientation(1) # HORIZONTAL = 0, VERTICAL = 1
