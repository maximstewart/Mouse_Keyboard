# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .columns import Left_Column, Keys_Column, Right_Column
from .signals_mixin import SignalsMixin



class Container(SignalsMixin, Gtk.Box):
    """docstring for Container."""

    def __init__(self):
        super(Container, self).__init__()

        self.setup_custom_event_signals()
        self.setup_styling()
        self.add_columns()

        self.show_all()


    def setup_styling(self):
        self.set_orientation(0)  # HORIZONTAL = 0, VERTICAL = 1
        self.set_vexpand(True)

    def setup_signals(self):
        pass

    def add_columns(self):
        self.add(Left_Column())
        self.add(Keys_Column())
        self.add(Right_Column())
