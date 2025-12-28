# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib

# Application imports


class Key(Gtk.Button or Gtk.ToggleButton):
    def __init__(self, primary = "NULL", secondary = "NULL", iscontrol = False):
        super(Key, self).__init__()

        self.timer_id          = None
        self.iscontrol         = iscontrol
        self._primary_symbol   = primary
        self._secondary_symbol = secondary
        self._alt_symbol       = ''
        self._is_upper         = False
        self._is_symbol        = False
        self._is_emoji         = False
        self.isShiftOn         = False

        self._setup_styling()
        self._setup_signals()
        self._subscribe_to_events()
        self._setup_if_keycombo(secondary)


    def _setup_styling(self):
        self.set_label(self._primary_symbol)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press)
        self.connect("button-release-event", self._do_release)
        self.connect("toggle-emoji-keys", self.toggle_emoji_keys)

    def _subscribe_to_events(self):
        event_system.subscribe("toggle_caps", self.toggle_caps)
        event_system.subscribe("toggle_symbol_keys", self.toggle_symbol_keys)

    def _setup_if_keycombo(self, secondary: str):
        if not self.iscontrol and (len(secondary) > 1 and '|' in secondary):
            self._secondary_symbol = secondary[0]

            parts = secondary.split("|")[1].split("+")
            for part in parts:
                if "shift" == part.lower():
                    self.isShiftOn = True

            self._alt_symbol = parts[-1]


    def _do_press(self, widget = None, eve = None):
        if not self.timer_id:
            self.did_loop_type = False
            self.timer_id = GLib.timeout_add(500, self._do_wait_loop_type)


    def _do_release(self, widget = None, eve = None):
        if self.did_loop_type:
            GLib.source_remove(self.timer_id)
            self.timer_id      = None
            self.did_loop_type = False
            return

        self._do_type()
        GLib.source_remove(self.timer_id)
        self.timer_id = None

    def _do_wait_loop_type(self):
        if not self.timer_id: return False
        self.did_loop_type = True
        self.timer_id = GLib.timeout_add(200, self._do_type)
        return False

    def _do_type(self):
        if not self.timer_id: return False

        key = self.get_label().strip()
        if self._is_emoji:
            typwriter.set_clipboard_data(key, "utf-16")
            typwriter.isCtrlOn = True
            typwriter.type('v')
            typwriter.isCtrlOn = False

            return True

        if self._alt_symbol and self._is_symbol:
            typwriter.isShiftOn = self.isShiftOn
            typwriter.type(self._alt_symbol)
            typwriter.isShiftOn = False

            return True

        typwriter.type(key)
        return True


    def _do_press_special_key(self, widget = None, eve = None):
        if not self.timer_id:
            self.did_loop_type = False
            self.timer_id = GLib.timeout_add(500, self._do_wait_loop_special_type)

    def _do_release_special_key(self, widget = None, eve = None):
        if self.did_loop_type:
            GLib.source_remove(self.timer_id)
            self.timer_id      = None
            self.did_loop_type = False
            return

        self._do_type_special_key()
        GLib.source_remove(self.timer_id)
        self.timer_id = None

    def _do_wait_loop_special_type(self):
        if not self.timer_id: return False
        self.did_loop_type = True
        self.timer_id = GLib.timeout_add(200, self._do_type_special_key)
        return False

    def _do_type_special_key(self):
        if not self.timer_id: return False

        key = self.get_label()
        if key in ["Ctrl", "Shift", "Alt"]:
            ctx = self.get_style_context()
            ctx.remove_class("toggled_bttn") if ctx.has_class("toggled_bttn") else ctx.add_class("toggled_bttn")

        typwriter.press_special_keys(key)
        return True


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
