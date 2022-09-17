# Python imports

# Lib imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from ..widgets.defined_keys import Tab_Key, Del_Key, Ctrl_Key, Shift_Key, Alt_Key, PrtSc_Key, Up_Key, Down_Key, Left_Key, Right_Key




class Button_Box(Gtk.ButtonBox):
    """docstring for Button_Box."""

    def __init__(self):
        super(Button_Box, self).__init__()

        for key in [Tab_Key(), Del_Key(), Ctrl_Key(), Shift_Key(), Alt_Key(), PrtSc_Key()]:
            self.add(key)

class List_Box(Gtk.ScrolledWindow):
    """docstring for List_Box."""

    def __init__(self):
        super(List_Box, self).__init__()

        self.setup_styling()
        tree, store = self.create_treeview()

        self.add(tree)
        self.set_size_request(360, 240)

    def setup_styling(self):
        self.set_vexpand(True)

    def create_treeview(self):
        tree   = Gtk.TreeView()
        store  = Gtk.ListStore(str)
        column = Gtk.TreeViewColumn("Commands")
        name   = Gtk.CellRendererText()
        selec  = tree.get_selection()

        tree.set_model(store)
        selec.set_mode(2)

        column.pack_start(name, True)
        column.add_attribute(name, "text", 0)
        column.set_expand(False)

        tree.append_column(column)
        tree.set_search_column(0)
        tree.set_headers_visible(True)
        tree.set_enable_tree_lines(False)

        tree.columns_autosize()
        return tree, store

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

        self. setup_styling()

        for key in [Button_Box(), List_Box(), Grid_Box()]:
            self.add(key)

        self.show_all()

    def setup_styling(self):
        self.set_orientation(1)  # HORIZONTAL = 0, VERTICAL = 1
        self.set_vexpand(True)
        self.set_margin_start(10)
        self.set_margin_end(10)
