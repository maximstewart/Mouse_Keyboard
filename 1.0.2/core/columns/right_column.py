# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.key import Key




class Backspace_Key(Key):
    def __init__(self):
        super(Backspace_Key, self).__init__("Backspace", "Backspace")


    def setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        typwriter.press_special_keys(self.get_label())

class Enter_Key(Key):
    def __init__(self):
        super(Enter_Key, self).__init__("Enter", "Enter")
        self.set_vexpand(True)


    def setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        typwriter.press_special_keys(self.get_label())


class Right_Column(Gtk.Box):
    """docstring for Right_Column."""

    def __init__(self):
        super(Right_Column, self).__init__()

        self.set_orientation(1) # HORIZONTAL = 0, VERTICAL = 1

        self.add(Backspace_Key())
        self.add(Enter_Key())
        self.show_all()
