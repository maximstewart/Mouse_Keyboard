# Python imports
import json
import time

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

try:
    from fast_autocomplete import AutoComplete
    auto_completion = True
except Exception as e:
    print( repr(e) )
    auto_completion = False

# Application imports
from .columns import Left_Column
from .columns import Keys_Column
from .columns import Right_Column
from .columns import Controls_Column




class Auto_Type(Gtk.Box):
    """docstring for Auto_Type."""

    def __init__(self):
        super(Auto_Type, self).__init__()

        self._processing_dictionary = False
        pad1              = Gtk.Label()
        pad2              = Gtk.Label()
        self._res_popover = Gtk.Popover()
        self._auto_typer  = Gtk.SearchEntry()
        self._type_btn    = Gtk.Button(label = "Type")

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

        self.setup_auto_completion()
        self.setup_styling()
        self.setup_signals()
        self.show_all()

    def setup_auto_completion(self):
        if auto_completion:
            self._word_list = Gtk.Box()
            scrolled_win    = Gtk.ScrolledWindow()
            viewport        = Gtk.Viewport()

            viewport.add(self._word_list)
            scrolled_win.add(viewport)
            scrolled_win.show_all()

            self._res_popover.set_size_request(200, 400)
            self._res_popover.set_relative_to(self._auto_typer)
            self._res_popover.set_modal(False)
            self._res_popover.add(scrolled_win)
            self._res_popover.set_default_widget(scrolled_win)

            self._word_list.set_orientation(Gtk.Orientation.VERTICAL)

            self.setup_dictionary()

    @daemon_threaded
    def setup_dictionary(self):
        self._processing_dictionary = True

        _words = set()
        words  = {}
        with open(DICT_FILE, 'r') as f:
            dict_data = json.load(f)
            self._auto_typer.set_progress_fraction(0.25)

            for field in dict_data:
                _words.add( field["word"] )
                _words.add( field["word"].lower()  )

            self._auto_typer.set_progress_fraction(0.5)
            del dict_data
            for word in _words:
                words[word] = {}

            self._auto_typer.set_progress_fraction(0.75)
            self.autocomplete = AutoComplete(words=words)
            del _words
            del words

        self._auto_typer.set_progress_fraction(1.0)
        time.sleep(1)
        self._auto_typer.set_progress_fraction(0.0)
        self._processing_dictionary = False

    def setup_styling(self):
        self.set_margin_bottom(5)

    def setup_signals(self):
        if auto_completion:
            self._auto_typer.connect("search-changed", self.search_changed)

        self._auto_typer.connect("enter-notify-event", self.focus_entry)
        self._auto_typer.connect("leave-notify-event", self.unfocus_entry)
        self._type_btn.connect("released", self.type_out)

    def focus_entry(self, widget, eve = None):
        event_system.emit("set_focusable")
        widget = self.get_children()[1]
        widget.grab_focus()

    def unfocus_entry(self, widget, eve = None):
        widget = self.get_children()[1]
        widget.grab_remove()
        event_system.emit("unset_focusable")

    def search_changed(self, widget = None, eve = None):
        if self._processing_dictionary: return

        text = widget.get_text()
        if not text:
            self._res_popover.hide()
            return

        words = self.autocomplete.search(word=text, max_cost=3, size=100)
        if not words:
            self._res_popover.hide()
            return

        self._clear_children(self._word_list)
        for word in words:
            button = Gtk.Button(label=word[0])
            button.connect("clicked", self.type_out)
            self._word_list.add(button)

        self._word_list.show_all()
        self._res_popover.show()

    def _clear_children(self, widget):
        for child in widget.get_children():
            widget.remove(child)

    def type_out(self, widget = None, eve = None):
        text = self._auto_typer.get_text()

        if isinstance(widget, Gtk.Button):
            if not widget.get_label().lower() == "type":
                text = widget.get_label()

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