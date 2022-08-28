# Python imports
import os

# Lib imports
import gi, cairo
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

# Application imports
from .signals_mixin import SignalsMixin
from .container import Container



class Window(SignalsMixin, Gtk.ApplicationWindow):
    """docstring for Window."""

    def __init__(self, args, unknownargs):
        super(Window, self).__init__()

        self._SCRIPT_PTH = os.path.dirname(os.path.realpath(__file__))
        self._ICON_FILE  = f"{self._SCRIPT_PTH}/../resources/icon.png"
        self._CSS_FILE   = f"{self._SCRIPT_PTH}/../resources/stylesheet.css"


        self.setup_win_settings()
        self.setup_styling()
        self.setup_signals()
        self.setup_custom_event_signals()
        self.add(Container())

        self.show_all()


    def setup_signals(self):
        self.connect("delete-event", Gtk.main_quit)

    def setup_win_settings(self):
        self.set_icon_from_file(self._ICON_FILE)
        self.set_title(app_name)
        self.set_default_size(800, 200)
        self.set_keep_above(True)
        self.set_accept_focus(False)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_type_hint(3) # 3 = TOOLBAR
        self.set_gravity(8)   # 5 = CENTER, 8 = SOUTH
        self.set_position(1)  # 1 = CENTER, 4 = CENTER_ALWAYS
        self.stick()

    def setup_styling(self):
        screen = self.get_screen()
        visual = screen.get_rgba_visual()

        if visual != None and screen.is_composited():
            self.set_visual(visual)
            self.set_app_paintable(True)
            self.connect("draw", self._area_draw)

        css_provider  = Gtk.CssProvider()
        css_provider.load_from_path(self._CSS_FILE)
        screen        = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def _area_draw(self, widget, cr):
        cr.set_source_rgba(0, 0, 0, 0.54)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)
