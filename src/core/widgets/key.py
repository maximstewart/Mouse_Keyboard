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
        self._is_symbol        = False

        self.set_label(self._primary_symbol)
        self.setup_signals()


    def setup_signals(self):
        self.connect("released", self._do_type)
        self.connect("toggle-caps", self.toggle_caps)
        self.connect("toggle-symbol-keys", self.toggle_symbol_keys)

    def _do_type(self, widget = None):
        key = self.get_label().strip()
        typwriter.type(key)

    def _do_press_special_key(self, widget = None):
        typwriter.press_special_keys(self.get_label())

    def toggle_symbol_keys(self, widget = None, eve = None):
        self._is_symbol = not self._is_symbol
        if self._is_symbol:
            self.set_label(self._secondary_symbol)
        else:
            self.set_label(self._primary_symbol.upper()) if self._is_upper else self.set_label(self._primary_symbol.lower())

    def toggle_caps(self, widget = None, eve = None):
        self._is_upper = not self._is_upper
        if not self._is_symbol:
            self.set_label(self._primary_symbol.upper()) if self._is_upper else self.set_label(self._primary_symbol.lower())
