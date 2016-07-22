#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from menu import *
from buttons import * #ScreenSwitchBtn, OptionBtn, LoadBookBtn
from book import *

class GameScreen(Screen):
    Options = []
    def play(self):
        book1 = Book()
        book1.load('/storage/sdcard0/com.hipipal.qpyplus/projects/TBA_kivy/story1.json')
        page_no = 0
    def flip_page(self, book, new_page=0):
        book.active_page = new_page
        main_dialog.text = book.book[new_page].para
        for i in range(4):
            self.Options[i].text = book.book.options[i]
            #self.Options[i].
        pass
    def build(self):
        print('GameScreen.build')
        self.size = Window.size
        main_dialog = Label()
        main_dialog.top = self.top
        main_dialog.center_x = self.center_x
        main_dialog.text = 'main dialog'
        self.add_widget(main_dialog)
        for i in range(4):
            opt = OptionBtn()
            opt.text = 'option ' + str(i)
            opt.size = self.width, 100
            opt.pos = 0, 100*(i+1)
            self.Options.insert(0,opt)
            self.add_widget(opt)
        btn = ScreenSwitchBtn()
        btn.text = 'menu'
        btn.id = 'to menu'
        btn.size = self.width, 100
        btn.pos = 0,0
        self.add_widget(btn)
        
class Settings(Screen):
    def build(self):
        print('Settings.build')
        self.size = Window.size
        opt = ScreenSwitchBtn()
        opt.text = 'back to menu'
        opt.size = self.width, 100
        opt.pos = 0,0
        opt.id = 'to menu'
        self.add_widget(opt)
        opt2 = LoadBookBtn()
        opt2.text = 'load story'
        opt2.size = self.width, 100
        opt2.pos = 0, 100
        def on_press(opt2):
            self.text = 'loaded'
        self.add_widget(opt2)
            
class MenuScreen(Screen):
    def build(self):
        print('MenuScreen.build')
        self.size = Window.size
        btn1 = ScreenSwitchBtn()
        btn1.text = 'game'
        btn1.size = self.width, 100
        btn1.pos = 0,100
        btn1.id = 'to game'
        self.add_widget(btn1)
        self.btn2 = ScreenSwitchBtn()
        self.btn2.text = 'settings'
        self.btn2.size = self.width, 100
        self.btn2.pos = 0,0
        self.btn2.id = 'to settings'
        self.add_widget(self.btn2)

class TBA(App):
    def build(self):
        print('TBA.build')
        sm = ScreenManager()
        print('creating menu screen...')
        menu = MenuScreen(name='main menu')
        menu.build()
        sm.add_widget(menu)
        print('...done')
        print('creating game screen...')
        game = GameScreen(name='game')
        game.build()
        sm.add_widget(game)
        print('...done')
        print('creating settings screen...')
        settings = Settings(name='settings')
        settings.build()
        sm.add_widget(settings)
        print('...done')
        return sm

TBA().run()

