# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.key import Key




class AT_Key(Key):
    def __init__(self):
        super(AT_Key, self).__init__("@", "@")

class Space_Key(Key):
    def __init__(self):
        super(Space_Key, self).__init__("Space", "Space")


    def setup_signals(self):
        self.connect("released", self._clicked)

    def _clicked(self, widget = None):
        typwriter.press_special_keys(self.get_label())

class COM_Key(Key):
    def __init__(self):
        super(COM_Key, self).__init__(".com", ".com")


    def setup_signals(self):
        self.connect("released", self._clicked)


class Bottom_Key_Row(Gtk.Box):
    def __init__(self):
        super(Bottom_Key_Row, self).__init__()

        self.set_property("homogeneous", True)

        for key in [AT_Key(), Space_Key(), COM_Key()]:
            self.add(key)

    def tempMethod(self, widget, data=None):
        pass
