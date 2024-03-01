# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.defined_keys import Symbols_Key
from ..widgets.defined_keys import Del_Key
from ..widgets.defined_keys import Ctrl_Key
from ..widgets.defined_keys import Shift_Key
from ..widgets.defined_keys import Alt_Key
from ..widgets.defined_keys import PrtSc_Key
from ..widgets.defined_keys import Up_Key
from ..widgets.defined_keys import Down_Key
from ..widgets.defined_keys import Left_Key
from ..widgets.defined_keys import Right_Key




class Button_Box(Gtk.ButtonBox):
    """docstring for Button_Box."""

    def __init__(self):
        super(Button_Box, self).__init__()

        for key in [Symbols_Key(), Del_Key(), Ctrl_Key(), Shift_Key(), Alt_Key(), PrtSc_Key()]:
            self.add(key)


class List_Box(Gtk.ScrolledWindow):
    """docstring for List_Box."""

    def __init__(self):
        super(List_Box, self).__init__()

        self.setup_styling()
        self.add_custom_signals()
        self.add_widgets()
        self._starting()


    def setup_styling(self):
        self.set_vexpand(True)

    def add_custom_signals(self):
        event_system.subscribe("shutting-down", self._shutting_down)
        event_system.subscribe("run_command", self.run_command)
        event_system.subscribe("add_command", self.add_command)
        event_system.subscribe("del_command", self.del_command)

    def add_widgets(self):
        self.tree, self.store = self.create_treeview()

        self.add(self.tree)
        self.set_size_request(360, 240)

    def create_treeview(self):
        tree   = Gtk.TreeView()
        store  = Gtk.ListStore(str)
        column = Gtk.TreeViewColumn("Commands")
        name   = Gtk.CellRendererText()
        selec  = tree.get_selection()

        tree.set_model(store)
        selec.set_mode(Gtk.SelectionMode.MULTIPLE)

        column.pack_start(name, True)
        column.add_attribute(name, "text", 0)
        column.set_expand(False)

        tree.append_column(column)
        tree.set_search_column(0)
        tree.set_headers_visible(True)
        tree.set_enable_tree_lines(False)

        tree.set_can_focus(False)
        tree.columns_autosize()

        tree.connect("row-activated", self._row_activated)

        return tree, store

    def _starting(self):
        file = f"{CONFIG_PATH}/commands_file.text"

        import os
        if not  os.path.exists(file): return

        commands = []
        with open(file, "r") as f:
            commands = f.readlines()

        for command in commands:
            self.store.append([command.strip()])

    def _shutting_down(self):
        commands = ""
        itr      = self.store.get_iter_first()

        while itr:
            commands += f"{self.store.get_value(itr, 0)}\n"
            itr = self.store.iter_next(itr)

        with open(f"{CONFIG_PATH}/commands_file.text", "w+") as f:
            f.write( commands.strip() )

    def _row_activated(self, tree_view, path, column):
        itr         = self.store.get_iter(path)
        command     = self.store.get_value(itr, 0)
        use_special = False

        for arg in LSIDE_KEYS + RSIDE_KEYS + FKEYS:
            if arg in command:
                use_special = True
                break

        if use_special:
            self.handle_as_special(command)
        else:
            typwriter.type(command)

    def run_command(self):
        ...

    def add_command(self, command):
        self.store.append([command])

    def del_command(self):
        path, column = self.tree.get_cursor()

        if not path or not column: return

        model = self.tree.get_model()
        itr   = model.get_iter(path)

        if not itr: return

        self.store.remove(itr)

    def handle_as_special(self, command):
        lside_count = []
        rside_count = []

        for arg in LSIDE_KEYS:
            lside_count.append( command.count(arg) )

        for arg in RSIDE_KEYS:
            rside_count.append( command.count(arg) )

        if not lside_count == rside_count:
            logger.info("Special keys don't match in open/close count...")
            return

        typwriter.press_special_keys(command)


class CommandEntry(Gtk.Box):
    """docstring for CommandEntry."""

    def __init__(self):
        super(CommandEntry, self).__init__()

        self.setup_styling()
        self.add_widgets()


    def setup_styling(self):
        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.set_hexpand(True)
        self.set_margin_top(5)
        self.set_margin_bottom(10)

    def add_widgets(self):
        entry    = Gtk.Entry()
        add_btn  = Gtk.Button(label = "+")
        del_btn  = Gtk.Button(label = "-")
        run_btn  = Gtk.Button(label = "RUN >")

        add_btn.set_always_show_image(True)
        del_btn.set_always_show_image(True)

        entry.set_hexpand(True)
        entry.set_placeholder_text("Command...")
        entry.set_tooltip_text("Command...")

        entry.connect("enter-notify-event", self.focus_entry)
        entry.connect("leave-notify-event", self.unfocus_entry)

        add_btn.connect("clicked", self.add_command)
        del_btn.connect("clicked", self.del_command)
        run_btn.connect("clicked", self.run_command)

        for widget in [run_btn, entry, add_btn, del_btn]:
            self.add(widget)

    def focus_entry(self, widget, eve = None):
        event_system.emit("set_focusable")
        widget = self.get_children()[1]
        widget.grab_focus()

    def unfocus_entry(self, widget, eve = None):
        widget = self.get_children()[1]
        widget.grab_remove()
        event_system.emit("unset_focusable")

    def run_command(self, button):
        event_system.emit("run_command")

    def add_command(self, button):
        command = self.get_children()[1].get_text().strip()
        if command:
            event_system.emit("add_command", command)

    def del_command(self, button):
        event_system.emit("del_command")


class Grid_Box(Gtk.Grid):
    """docstring for Grid_Box."""

    def __init__(self):
        super(Grid_Box, self).__init__()

        self.setup_styling()

        self.insert_row(0)
        self.insert_row(1)
        self.insert_row(2)
        self.insert_column(0)
        self.insert_column(1)
        self.insert_column(2)

        # NOTE: Widget, left, top, width, height
        self.attach(Up_Key(), 1, 0, 1, 1)
        self.attach(Down_Key(), 1, 2, 1, 1)
        self.attach(Left_Key(), 0, 1, 1, 1)
        self.attach(Right_Key(), 2, 1, 1, 1)


    def setup_styling(self):
        self.set_margin_top(5)
        self.set_margin_bottom(5)
        self.set_column_homogeneous(True)


class Controls_Column(Gtk.Box):
    """docstring for Controls_Column."""

    def __init__(self):
        super(Controls_Column, self).__init__()

        self.setup_styling()

        for key in [Button_Box(), List_Box(), CommandEntry(), Grid_Box()]:
            self.add(key)

        self.show_all()


    def setup_styling(self):
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_vexpand(True)
        self.set_margin_start(10)
        self.set_margin_end(10)
