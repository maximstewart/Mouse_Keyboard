# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports




class Right_Column(Gtk.Button):
    """docstring for Right_Column."""

    def __init__(self):
        super(Right_Column, self).__init__()

        self.setup_styling()
        self.setup_signals()
        self.show_all()


    def setup_styling(self):
        self.set_label("Enter")

    def setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        typwriter.enter()
