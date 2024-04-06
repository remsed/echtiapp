from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = """

ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: "login"
    MDLabel:
        text: "Sign-in to your account"
        font_size: "23sp"
        color: 100/255, 100/255, 1000/255, 1
        pos_hint: {"center_x": .5, "center_y": .90}
        halign: 'center'
        valign: 'middle'
    MDTextField:
        id: user_name
        hint_text: "Username"
        mode: "rectangle"
        pos_hint: {"center_x": .5, "center_y": .80}
        size_hint_x: .5
        icon_left: "account"
    MDTextField:
        id: pass_word
        hint_text: "Password"
        mode: "rectangle"
        pos_hint: {"center_x": .5, "center_y": .70}
        size_hint_x: .5
        password: True
        icon_left: "key-variant"
    MDFillRoundFlatIconButton:
        text: "LOGIN"
        icon: "login"
        pos_hint: {"center_x": .5, "center_y": .60}
        on_press: root.manager.current = 'home'
    MDFillRoundFlatIconButton:
        text: "SIGN-UP"
        icon: "account-plus"
        pos_hint: {"center_x": .5, "center_y": .50}

<HomeScreen>:
    name: "home"
    MDLabel:
        text: "test"
        font_size: "23sp"
        color: 100/255, 100/255, 1000/255, 1
        pos_hint: {"center_x": .5, "center_y": .90}
        halign: 'center'
        valign: 'middle'

"""

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(LoginScreen(name='login'))
screen_manager.add_widget(HomeScreen(name='home'))


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        screen = Builder.load_string(KV)
        return screen

if __name__ == '__main__':
    MainApp().run()