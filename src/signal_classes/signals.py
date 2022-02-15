# Python imports
import threading, subprocess, os

# Gtk imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Application imports
from .mixins.keyboardmixin import KeyboardMixin


def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper


class Signals(KeyboardMixin):
    def __init__(self, settings):
        self.settings       = settings
        self.builder        = self.settings.returnBuilder()
        self.autoTypeField  = self.builder.get_object("autoTypeField")
        self.commandsStore  = self.builder.get_object("commands")
        self.specialsStore  = self.builder.get_object("specials")
        self.specialsTree   = self.builder.get_object("specialsTree")
        main_keys           = self.builder.get_object("main_keys")

        self.isCapsLockOn   = False
        self.isCtrlOn       = False
        self.isShiftOn      = False
        self.isAltOn        = False

        special_characters  = "<>()[]{}/\!?#$%&@*:^|'\"-_=+~`"
        self.generate_keys(special_characters, self.specialsStore)
        self.specialsStore.show_all()
        main_keys.show_all()

        row1_characters = "1234567890"
        row1            = Gtk.Box()
        self.generate_keys(["Esc",], row1)
        self.generate_keys(row1_characters, row1)
        self.generate_keys(["Backspace",], row1)
        row1.set_homogeneous(True)
        row1.show_all()
        main_keys.add(row1)

        row2_characters = "qwertyuiop"
        row2            = Gtk.Box()
        self.generate_keys(["Tab",], row2)
        self.generate_keys(row2_characters, row2)
        row2.set_homogeneous(True)
        row2.show_all()
        main_keys.add(row2)

        row3_characters = "asdfghjkl"
        row3            = Gtk.Box()
        self.generate_keys(["Caps Lock",], row3)
        self.generate_keys(row3_characters, row3)
        self.generate_keys(["Enter",], row3)
        row3.set_homogeneous(True)
        row3.show_all()
        main_keys.add(row3)

        row4_characters = "zxcvbnm,.:"
        row4            = Gtk.Box()
        self.generate_keys(row4_characters, row4)
        row4.set_homogeneous(True)
        row4.show_all()
        main_keys.add(row4)

        row5_characters = "Space"
        row5            = Gtk.Box()
        self.generate_keys([row5_characters,], row5)
        row5.set_homogeneous(True)
        row5.show_all()
        main_keys.add(row5)


    def generate_keys(self, labels, target):
        for label in labels:
            button = Gtk.Button.new_with_label(label)
            if label not in ["Enter", "Backspace", "Caps Lock"]:
                button.connect("clicked", self.insert)
            else:
                if label == "Enter":
                    button.connect("clicked", self.enter)
                if label == "Backspace":
                    button.connect("clicked", self.backspace)
                if label == "Caps Lock":
                    button = Gtk.ToggleButton.new_with_label(label)
                    button.connect("toggled", self.toggleCaps)

            target.add(button)


    def getClipboardData(self):
        proc    = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
        retcode = proc.wait()
        data    = proc.stdout.read()
        return data.decode("utf-8").strip()

    def setClipboardData(self, data):
        proc = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
        proc.stdin.write(data)
        proc.stdin.close()
        retcode = proc.wait()
