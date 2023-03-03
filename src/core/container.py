# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .columns import Left_Column
from .columns import Keys_Column
from .columns import Right_Column
from .columns import Controls_Column




class Auto_Type(Gtk.Box):
    """docstring for Auto_Type."""

    def __init__(self):
        super(Auto_Type, self).__init__()

        pad1             = Gtk.Label()
        pad2             = Gtk.Label()
        self._auto_typer = Gtk.SearchEntry()
        self._type_btn   = Gtk.Button(label="Type")

        self._auto_typer.set_placeholder_text("Autotype Field...")
        self._auto_typer.set_icon_from_stock(0, "gtk-go-forward") # PRIMARY = 0, SECONDARY = 1
        self._auto_typer.set_can_focus(True)
        self._auto_typer.set_hexpand(True)

        pad1.set_hexpand(True)
        pad2.set_hexpand(True)

        self.add(pad1)
        self.add(self._auto_typer)
        self.add(self._type_btn)
        self.add(pad2)

        self.setup_styling()

        self.setup_signals()
        self.show_all()

    def setup_styling(self):
        self.set_margin_bottom(5)

    def setup_signals(self):
        self._type_btn.connect("released", self.type_out)

    def type_out(self, widget = None, eve = None):
        text = self._auto_typer.get_text()
        typwriter.type_string(text)


class Main_Container(Gtk.Box):
    """docstring for Main_Container."""

    def __init__(self):
        super(Main_Container, self).__init__()

        self.setup_styling()
        self.add_columns()

        self.show_all()


    def setup_styling(self):
        self.set_orientation(0)  # HORIZONTAL = 0, VERTICAL = 1
        self.set_vexpand(True)

    def add_columns(self):
        self.add(Left_Column())
        self.add(Keys_Column())
        self.add(Right_Column())
        self.add(Controls_Column())


class Container(Gtk.Box):
    """docstring for Container."""

    def __init__(self):
        super(Container, self).__init__()

        self.setup_styling()
        self.add_content()

        self.show_all()


    def setup_styling(self):
        self.set_orientation(1)  # HORIZONTAL = 0, VERTICAL = 1
        self.set_vexpand(True)
        self.set_margin_start(5)
        self.set_margin_top(5)
        self.set_margin_bottom(5)

    def add_content(self):
        self.add(Auto_Type())
        self.add(Main_Container())
