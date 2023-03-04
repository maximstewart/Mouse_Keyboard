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

            top  = 0
            left = 0
            for emoji in emoji_grouping[group]:
                key = Key(emoji["emoji"], emoji["emoji"])
                key._is_emoji = True
                grid.attach(key, left, top, width, height)

                left += 1
                if left > 8:
                    left = 0
                    top += 1

            self.append_page(scroll, tab_widget)
            self.set_tab_reorderable(scroll, False)
            self.set_tab_detachable(scroll, False)

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
        self.set_default_widget(emoji_notebook)
        self.setup_styling()

        self._emoji_key = None


    def setup_styling(self):
        self.set_vexpand(True)
        self.set_size_request(480, 280)

    def setup_signals(self):
        self.connect("closed", self._emoji_key.unset_selected)

    def set_parent_key(self, emoji_key):
        self._emoji_key = emoji_key
        self.setup_signals()
