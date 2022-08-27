# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports




class Left_Column(Gtk.Button):
    """docstring for Left_Column."""

    def __init__(self):
        super(Left_Column, self).__init__()

        self.setup_styling()
        self.setup_signals()
        self.show_all()


    def setup_styling(self):
        self.set_label("Caps")

    def setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        key_columns = self.get_parent().get_children()[1]
        limit = len(key_columns.get_children()) - 1

        for i, row in enumerate(key_columns.get_children()):
            if not i == limit:
                for key in row:
                    key.emit("toggle-caps", ())
