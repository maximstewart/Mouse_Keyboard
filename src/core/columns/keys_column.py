# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.key import Key
from ..bottom_key_row import Bottom_Key_Row


class KeyboardRowMatchError(Exception):
    pass


class Keys_Column(Gtk.Box):
    """docstring for Keys_Column."""

    def __init__(self):
        super(Keys_Column, self).__init__()

        self.setup_styling()
        self.setup_signals()
        self.setup_custom_signals()
        self.setup_key_buttons()

        self.show_all()


    def setup_styling(self):
        self.set_orientation(1)  # HORIZONTAL = 0, VERTICAL = 1
        self.set_property("homogeneous", True)
        self.set_hexpand(True)

    def setup_signals(self):
        self.connect("button-release-event", self._on_button_release_event)

    def setup_custom_signals(self):
        event_system.subscribe("itterate_mode", self.itterate_mode)

    def _on_button_release_event(self, widget = None, eve = None):
        if eve.button == 3: # NOTE: right-click
            event_system.emit_and_await("itterate_mode")

    def setup_key_buttons(self):
        keys = keys_set["keys"]
        children = keys.keys()

        for child in children:
            pKeys = keys[child]["pKeys"]
            sKeys = keys[child]["sKeys"]

            row_box = self.add_row()
            if len(pKeys) == len(sKeys):
                for i in range(10):
                    pkey = pKeys[i]
                    sKey = sKeys[i]
                    row_box.add(Key(pkey, sKey))
            else:
                raise KeyboardRowMatchError("A row in keys_json has missmatched pKeys to sKeys lengths.")

        self.add(Bottom_Key_Row())


    def add_row(self):
        row_box = Gtk.Box()
        row_box.set_property("homogeneous", True)
        self.add(row_box)

        return row_box

    def itterate_mode(self):
        emoji_view_shown   = event_system.emit_and_await("is_emoji_view_shown")
        is_symbols_enabled = event_system.emit_and_await("is_symbols_enabled")

        if not is_symbols_enabled and not emoji_view_shown:
            event_system.emit("toggle_symbol_keys")
        elif is_symbols_enabled and not emoji_view_shown:
            event_system.emit("show_emoji_view")
        elif is_symbols_enabled and emoji_view_shown:
            event_system.emit("hide_emoji_view")
            event_system.emit("toggle_symbol_keys")
