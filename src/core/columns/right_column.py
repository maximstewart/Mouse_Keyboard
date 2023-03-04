# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.emoji_popover import Emoji_Popover
from ..widgets.defined_keys import Emoji_Key
from ..widgets.defined_keys import Backspace_Key
from ..widgets.defined_keys import Enter_Key




class Right_Column(Gtk.Box):
    """docstring for Right_Column."""

    def __init__(self):
        super(Right_Column, self).__init__()

        self.setup_styling()

        emoji_popover = Emoji_Popover()
        emoji_key     = Emoji_Key(emoji_popover)

        emoji_popover.set_parent_key(emoji_key)
        emoji_popover.set_relative_to(emoji_key)
        emoji_popover.set_constrain_to(0)  # LEFT = 0, RIGHT = 1, TOP = 2, BOTTOM = 3

        for key in [emoji_key, Backspace_Key(), Enter_Key()]:
            self.add(key)

        self.show_all()

    def setup_styling(self):
        self.set_orientation(1) # HORIZONTAL = 0, VERTICAL = 1
