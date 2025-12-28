# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .key import Key




##############################  Left_Column Keys  ##############################

class Esc_Key(Key):
    def __init__(self):
        super(Esc_Key, self).__init__("Esc", "Esc", iscontrol = True)

    def _setup_signals(self):
        self.connect("released", self._do_press_special_key)

class CAPS_Key(Key):
    def __init__(self):
        super(CAPS_Key, self).__init__("Caps", "Caps", iscontrol = True)

        self._setup_styling()

    def _setup_styling(self):
        self.set_vexpand(True)
        super()._setup_styling()

    def _setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        ctx = widget.get_style_context()
        ctx.remove_class("toggled_bttn") if ctx.has_class("toggled_bttn") else ctx.add_class("toggled_bttn")
        event_system.emit("toggle_caps")


##############################  Right_Column Keys  ##############################

class Backspace_Key(Key):
    def __init__(self):
        super(Backspace_Key, self).__init__("Backspace", "Backspace", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class Emoji_Key(Key):
    def __init__(self, emoji_popover):
        super(Emoji_Key, self).__init__("Emoji", "Emoji", iscontrol=True)

        self._ctx           = self.get_style_context()
        self._emoji_popover = emoji_popover

    def _setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        self._ctx.add_class("toggled_bttn")
        self._emoji_popover.popup()

    def unset_selected(self, widget = None):
        self._ctx.remove_class("toggled_bttn")

class Symbols_Key(Key):
    def __init__(self):
        super(Symbols_Key, self).__init__("Symbols", "Symbols", iscontrol = True)
        self.setup_custom_signals()

    def _setup_signals(self):
        self.connect("released", self._clicked)

    def setup_custom_signals(self):
        event_system.subscribe("is_symbols_enabled", self.is_symbols_enabled)
        event_system.subscribe("toggle_symbol_keys", self.toggle_symbol_keys)

    def _clicked(self, widget = None):
        ctx = widget.get_style_context()
        ctx.remove_class("toggled_bttn") if ctx.has_class("toggled_bttn") else ctx.add_class("toggled_bttn")
        event_system.emit("toggle_symbol_keys")

    def is_symbols_enabled(self):
        ctx = self.get_style_context()
        return True if ctx.has_class("toggled_bttn") else False

class Enter_Key(Key):
    def __init__(self):
        super(Enter_Key, self).__init__("Enter", "Enter", iscontrol=True)
        self._setup_styling()

    def _setup_styling(self):
        self.set_vexpand(True)
        super()._setup_styling()

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)


#############################  Bottom_Key_Row Keys  #############################

class Esc_Key(Key):
    def __init__(self):
        super(Esc_Key, self).__init__("Esc", "Esc", iscontrol=True)

    def _setup_signals(self):
        self.connect("released", self._do_press_special_key)

class Space_Key(Key):
    def __init__(self):
        super(Space_Key, self).__init__("Space", "Space", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class AT_Key(Key):
    def __init__(self):
        super(AT_Key, self).__init__("@", "@", iscontrol=True)

class COM_Key(Key):
    def __init__(self):
        super(COM_Key, self).__init__(".com", ".com")


############################  Controls_Column Keys  ############################

class Tab_Key(Key):
    def __init__(self):
        super(Tab_Key, self).__init__("Tab", "Tab", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class Del_Key(Key):
    def __init__(self):
        super(Del_Key, self).__init__("Del", "Del", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class Ctrl_Key(Key):
    def __init__(self):
        super(Ctrl_Key, self).__init__("Ctrl", "Ctrl", iscontrol=True)

    def _setup_signals(self):
        self.connect("released", self._do_press_special_key)

class Shift_Key(Key):
    def __init__(self):
        super(Shift_Key, self).__init__("Shift", "Shift", iscontrol=True)

    def _setup_signals(self):
        self.connect("released", self._do_press_special_key)

class Alt_Key(Key):
    def __init__(self):
        super(Alt_Key, self).__init__("Alt", "Alt", iscontrol=True)

    def _setup_signals(self):
        self.connect("released", self._do_press_special_key)

class PrtSc_Key(Key):
    def __init__(self):
        super(PrtSc_Key, self).__init__("PrtSc", "PrtSc", iscontrol=True)

    def _setup_signals(self):
        self.connect("released", self._do_press_special_key)

class Up_Key(Key):
    def __init__(self):
        super(Up_Key, self).__init__("Up", "Up", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class Down_Key(Key):
    def __init__(self):
        super(Down_Key, self).__init__("Down", "Down", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class Left_Key(Key):
    def __init__(self):
        super(Left_Key, self).__init__("Left", "Left", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)

class Right_Key(Key):
    def __init__(self):
        super(Right_Key, self).__init__("Right", "Right", iscontrol=True)

    def _setup_signals(self):
        self.connect("button-press-event", self._do_press_special_key)
        self.connect("button-release-event", self._do_release_special_key)
