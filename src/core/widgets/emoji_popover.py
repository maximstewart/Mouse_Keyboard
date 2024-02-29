# Python imports
from collections import defaultdict
import json

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .key import Key




class Emoji_Notebook(Gtk.Notebook):
    """docstring for Emoji_Notebook."""

    def __init__(self):
        super(Emoji_Notebook, self).__init__()

        self.load_ui( self.get_data(EMOJI_FILE) )

        self.setup_styling()
        self.show_all()


    def setup_styling(self):
        self.set_current_page(0)
        self.set_scrollable(True)

    def get_data(self, file):
        emoji_grouping = defaultdict(list)

        with open(file, 'r') as f:
            emoji_data = json.load(f)
            for emoji in emoji_data:
                category = emoji['category']
                del emoji['category']
                del emoji['unicode_version']
                del emoji['ios_version']
                emoji_grouping[category].append(emoji)

        return emoji_grouping

    def load_ui(self, emoji_grouping):
        width  = 1
        height = 1
        for group in emoji_grouping:
            tab_widget   = Gtk.Label(label=group)
            scroll, grid = self.create_scroll_and_grid()
            self.append_page(scroll, tab_widget)
            self.set_tab_reorderable(scroll, False)
            self.set_tab_detachable(scroll, False)

            top  = 0
            left = 0
            for emoji in emoji_grouping[group]:
                key = Key(emoji["emoji"], emoji["emoji"])
                key._is_emoji = True
                key.show()
                grid.attach(key, left, top, width, height)

                left += 1
                if left > 8:
                    left = 0
                    top += 1


    def create_scroll_and_grid(self):
        scroll = Gtk.ScrolledWindow()
        grid   = Gtk.Grid()
        scroll.add(grid)

        return scroll, grid



class Emoji_Popover(Gtk.Popover):
    """docstring for Emoji_Popover."""

    def __init__(self):
        super(Emoji_Popover, self).__init__()

        emoji_notebook = Emoji_Notebook()
        self.add(emoji_notebook)
        self.setup_styling()
        self.setup_signals()
        self.setup_custom_signals()

        self._emoji_key = None


    def setup_styling(self):
        self.set_vexpand(True)
        self.set_size_request(480, 280)

    def setup_signals(self):
        ...

    def setup_custom_signals(self):
        event_system.subscribe("is_emoji_view_shown", self.is_emoji_view_shown)
        event_system.subscribe("show_emoji_view", self.show_emoji_view)
        event_system.subscribe("hide_emoji_view", self.hide_emoji_view)

    def set_parent_key(self, emoji_key):
        self._emoji_key = emoji_key
        self.setup_signals()

    def is_emoji_view_shown(self):
        return self.is_visible()

    def show_emoji_view(self):
        self.popup()

    def hide_emoji_view(self):
        self.popdown()
