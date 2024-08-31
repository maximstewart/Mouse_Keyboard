# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports


class Key(Gtk.Button or Gtk.ToggleButton):
    def __init__(self, primary = "NULL", secondary = "NULL", iscontrol=False):
        super(Key, self).__init__()

        self.iscontrol         = iscontrol
        self._primary_symbol   = primary
        self._secondary_symbol = secondary
        self._is_upper         = False
        self._is_symbol        = False
        self._is_emoji         = False

        self.set_label(self._primary_symbol)
        self.setup_custom_signals()
        self.setup_signals()

    def setup_custom_signals(self):
        event_system.subscribe("toggle_caps", self.toggle_caps)
        event_system.subscribe("toggle_symbol_keys", self.toggle_symbol_keys)

    def setup_signals(self):
        self.connect("released", self._do_type)
        self.connect("toggle-emoji-keys", self.toggle_emoji_keys)

    def _do_type(self, widget = None):
        key = self.get_label().strip()
        if not self._is_emoji:
            typwriter.type(key)
        else:
            typwriter.set_clipboard_data(key, "utf-16")
            typwriter.isCtrlOn = True
            typwriter.type('v')
            typwriter.isCtrlOn = False

    def _do_press_special_key(self, widget = None):
        key = self.get_label()
        if key in ["Ctrl", "Shift", "Alt"]:
            ctx = widget.get_style_context()
            ctx.remove_class("toggled_bttn") if ctx.has_class("toggled_bttn") else ctx.add_class("toggled_bttn")

        typwriter.press_special_keys(key)

    def toggle_symbol_keys(self, widget = None, eve = None):
        if not self.iscontrol:
            self._is_symbol = not self._is_symbol
            if self._is_symbol:
                self.set_label(self._secondary_symbol)
            else:
                self.set_label(self._primary_symbol.upper()) if self._is_upper else self.set_label(self._primary_symbol.lower())

    # NOTE: Might use name attrib on widgets and de-duplicate this and the above logic.
    def toggle_emoji_keys(self, widget = None, eve = None):
        if not self.iscontrol:
            if self._is_symbol:
                self.set_label(self._secondary_symbol)
            else:
                self.set_label(self._primary_symbol.upper()) if self._is_upper else self.set_label(self._primary_symbol.lower())

    def toggle_caps(self, widget = None, eve = None):
        if not self.iscontrol:
            self._is_upper = not self._is_upper
            if not self._is_symbol:
                self.set_label(self._primary_symbol.upper()) if self._is_upper else self.set_label(self._primary_symbol.lower())