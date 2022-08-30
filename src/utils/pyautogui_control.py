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
        if self.isCtrlOn or self.isShiftOn or self.isAltOn:
            self.set_hotkeys()

        pyautogui.typewrite(key)

        if self.isCtrlOn or self.isShiftOn or self.isAltOn:
            self.unset_hotkeys()


    def enter(self, widget = None, data = None):
        pyautogui.press("enter")

    def backspace(self, widget = None, data=None):
        pyautogui.press("backspace")

    def press_special_keys(self, key):
        if key in ["Backspace", "Enter", "Esc", "Tab", "Space", "Del", "Up", "Down", "Left", "Right", "PrtSc"]:
            pyautogui.press(key.lower())
            return True

        if key in ["Ctrl", "Shift", "Alt"]:
            if key == "Ctrl":
                self.isCtrlOn  = not self.isCtrlOn
            if key == "Shift":
                self.isShiftOn = not self.isShiftOn
            if key == "Alt":
                self.isAltOn   = not self.isAltOn

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


    def set_hotkeys(self):
        if self.isCtrlOn:
            pyautogui.keyDown('ctrl')
        if self.isShiftOn:
            pyautogui.keyDown('shiftleft')
            pyautogui.keyDown('shiftright')
        if self.isAltOn:
            pyautogui.keyDown('alt')


    def unset_hotkeys(self):
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('alt')
