# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .container import Container



class Window(Gtk.ApplicationWindow):
    """docstring for Window."""

    def __init__(self, args, unknownargs):
        super(Window, self).__init__()

        self.setup_styling()
        self.setup_signals()
        self.add(Container())

        self.show_all()


    def setup_styling(self):
        # self.set_icon_from_file("/usr/share/bulkr/bulkr.png")
        self.set_title(app_name)
        self.set_default_size(800, 200)
        self.set_type_hint(3) # 3 = TOOLBAR
        self.set_gravity(8)   # 5 = CENTER, 8 = SOUTH
        self.set_position(1)  # 1 = CENTER, 4 = CENTER_ALWAYS
        self.stick()

    def setup_signals(self):
        self.connect("delete-event", Gtk.main_quit)
