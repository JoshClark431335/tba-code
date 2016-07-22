from kivy.uix.button import Button
from book import *

class ScreenSwitchBtn(Button):
    def on_press(self):
        print('ScreenSwitch.on_press')
        sm = self.parent.parent
        if self.id=='to game':
            sm.transition.direction = 'left'
            sm.current = 'game'
        elif self.id=='to menu':
            sm.transition.direction = 'right'
            sm.current = 'main menu'
        elif self.id=='to settings':
            sm.transition.direction = 'left'
            sm.current = 'settings'

class OptionBtn(Button):
    toggle = False
    link = 0
    def on_press(self):
        print('OptionBtn.on_press')
        self.toggle = not self.toggle
        if self.toggle:
            self.text = 'activated'
        else:
            self.text = 'deactivated'

class LoadBookBtn(Button):
    #size_hint = None, None
    def on_press(self):
        print('LoadBookBtn.on_press')
        self.text = 'loaded'
        book1 = Book()
        #book1.load('/storage/sdcard0/com.hipipal.qpyplus/projects/TBA_kivy/story1.json')
