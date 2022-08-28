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
        self.setup_key_buttons()

        self.show_all()


    def setup_styling(self):
        self.set_orientation(1)  # HORIZONTAL = 0, VERTICAL = 1
        self.set_property("homogeneous", True)
        self.set_hexpand(True)

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
                raise KeyboardRowMatchError("A row in keys_json has missmatched pKeys and sKeys lengths.")

        self.add(Bottom_Key_Row())


    def add_row(self):
        row_box = Gtk.Box()
        row_box.set_property("homogeneous", True)
        self.add(row_box)

        return row_box
