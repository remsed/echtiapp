from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
#from kivy.core.window import Window
#Window.size = (720, 1600)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager

if __name__ == '__main__':
    app = MainApp()
    app.run()