# Python imports
import pyautogui

# Gtk imports

# Application imports


# Let piautogui make updates as quick as it can...
pyautogui.FAILSAFE         = False    # If we hit corner, that's ok
pyautogui.MINIMUM_DURATION = 0
pyautogui.PAUSE            = 0


class ControlMixin:

    def type(self, key):
        pyautogui.typewrite(key)

    def enter(self, widget = None, data = None):
        pyautogui.press("enter")

    def backspace(self, widget = None, data=None):
        pyautogui.press("backspace")

    def press_special_keys(self, key):
        if key in ["Backspace", "Enter", "Esc", "Tab", "Space", "Del", "Up", "Down", "Left", "Right", "PrtSc"]:
            pyautogui.press(key.lower())
            return True

        for i in range(1, 13):
            fkey = 'F' + str(i)
            if key == fkey:
                pyautogui.press(key.lower())
                return True

        return False

    def type_string(self, text):
        for char in text:
            pyautogui.typewrite(char)





    # def typeString(self, widget = None, data = None):
    #     text = self.autoTypeField.get_text()
    #     for char in text:
    #         self.do_insert(char)
    #
    # def insert(self, widget = None, data = None, key = None):
    #     if not key:
    #         key = widget.get_label().strip()
    #
    #     if self.is_keypress_type(key):
    #         return
    #
    #     if self.isCapsLockOn:
    #         key = key.upper()
    #
    #     self.do_insert(key)
    #
    #
    # def do_insert(self, key):
    #     if self.isCtrlOn or self.isShiftOn or self.isAltOn:
    #         self.set_hotkeys()
    #
    #     pyautogui.typewrite(key)
    #
    #     if self.isCtrlOn or self.isShiftOn or self.isAltOn:
    #         self.unset_hotkeys()
    #
    #
    # def is_keypress_type(self, key):
    #     if key in ["Esc", "Tab", "Space", "Del", "Up", "Down", "Left", "Right", "PrtSc"]:
    #         pyautogui.press(key.lower())
    #         return True
    #
    #     for i in range(1, 13):
    #         fkey = 'F' + str(i)
    #         if key == fkey:
    #             pyautogui.press(key.lower())
    #             return True
    #
    #     return False
    #
    #
    # def set_hotkeys(self):
    #     if self.isCtrlOn:
    #         pyautogui.keyDown('ctrl')
    #     if self.isShiftOn:
    #         pyautogui.keyDown('shiftleft')
    #         pyautogui.keyDown('shiftright')
    #     if self.isAltOn:
    #         pyautogui.keyDown('alt')
    #
    #
    # def unset_hotkeys(self):
    #     pyautogui.keyUp('ctrl')
    #     pyautogui.keyUp('shiftleft')
    #     pyautogui.keyUp('shiftright')
    #     pyautogui.keyUp('alt')
    #
    #
    # def toggleCaps(self, widget, data=None):
    #     self.isCapsLockOn = False if self.isCapsLockOn else True
    #
    # def tgglCtrl(self, widget, data=None):
    #     self.isCtrlOn = False if self.isCtrlOn else True
    #
    # def tgglShift(self, widget, data=None):
    #     self.isShiftOn = False if self.isShiftOn else True
    #
    # def tgglAlt(self, widget, data=None):
    #     self.isAltOn = False if self.isAltOn else True
    #
    #
    # def enter(self, widget, data=None):
    #     pyautogui.press("enter")
    #
    #
    # def backspace(self, widget, data=None):
    #     pyautogui.press("backspace")
