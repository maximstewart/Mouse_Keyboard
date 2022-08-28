# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.key import Key

import traceback




class Symbols_Key(Key):
    def __init__(self):
        super(Symbols_Key, self).__init__("Symbols", "Symbols")


    def setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        key_columns = self.get_parent().get_parent().get_children()[1]

        for row in key_columns.get_children():
            for key in row:
                key.emit("toggle-symbol-keys", ())

class CAPS_Key(Gtk.ToggleButton):
    def __init__(self):
        super(CAPS_Key, self).__init__("Caps", "Caps")

        self.set_vexpand(True)

        self.setup_signals()
        self.show_all()


    def setup_signals(self):
        self.connect("clicked", self._clicked)

    def _clicked(self, widget = None):
        key_columns = self.get_parent().get_parent().get_children()[1]

        for row in key_columns.get_children():
            for key in row:
                key.emit("toggle-caps", ())


class Left_Column(Gtk.Box):
    """docstring for Left_Column."""

    def __init__(self):
        super(Left_Column, self).__init__()


        self.set_orientation(1) # HORIZONTAL = 0, VERTICAL = 1

        self.add(Symbols_Key())
        self.add(CAPS_Key())
        self.show_all()
