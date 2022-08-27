# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports


class Key(Gtk.Button):
    def __init__(self, primary = "NULL", secondary = "NULL"):
        super(Key, self).__init__()

        self._primary_symbol   = primary
        self._secondary_symbol = secondary
        self._is_upper         = False

        self.set_label(self._primary_symbol)

        self.setup_signals()


    def toggle_caps(self, widget = None, eve = None):
        self._is_upper = not self._is_upper
        self.set_label(self._primary_symbol.upper()) if self._is_upper else self.set_label(self._primary_symbol.lower())

    def setup_signals(self):
        self.connect("released", self._clicked)
        self.connect("toggle-caps", self.toggle_caps)

    def _clicked(self, widget = None):
        key = self.get_label().strip()
        typwriter.type(key)
