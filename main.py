# import all the relevant classes
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd


# class to call the popup function
class PopupWindow(Widget):
    def btn(self):
        popFun()


# class to build GUI for a popup window
class P(FloatLayout):
    pass


# function that displays the content
def popFun():
    show = P()
    window = Popup(title="popup", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


# class to accept user info and validate it
class loginWindow(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def validate(self):

        # validating if the email already exists
        users = pd.read_csv('login.csv')
        if self.email.text not in users['Email'].unique():
            popFun()
        else:

            # switching the current screen to display validation result
            sm.current = 'mainmenu'

            # reset TextInput widget
            self.email.text = ""
            self.pwd.text = ""

    def Erase(self):
        self.email.text = ""
        self.pwd.text = ""


# class to accept sign up info
class signupWindow(Screen):
    name2 = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def signupbtn(self):
        # creating a DataFrame of the info
        user = pd.DataFrame([[self.name2.text, self.email.text, self.pwd.text]],
                            columns=['Name', 'Email', 'Password'])
        if self.email.text != "":
            if self.email.text not in users['Email'].unique():
                # if email does not exist already then append to the csv file
                # change current screen to log in the user now
                user.to_csv('login.csv', mode='a', header=False, index=False)
                sm.current = 'login'
                self.name2.text = ""
                self.email.text = ""
                self.pwd.text = ""
            else:
                # if values are invalid show pop up
                popFun()
        else:
            # if values are empty show pop up
            popFun()


class mainmenuWindow(Screen):
    pass

    # class to display validation result


class logDataWindow(Screen):
    pass


class PechoWindow(Screen):
    btn = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)

    def newbtn(self):
        self.btn.background_color = "green"
    def newbtn1(self):
        self.btn1.background_color = "green"
    def newbtn2(self):
        self.btn2.background_color = "green"
    def newbtn3(self):
        self.btn3.background_color = "green"

class EspaldaWindow(Screen):
    btn = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)

    def newbtn(self):
        self.btn.background_color = "green"

    def newbtn1(self):
        self.btn1.background_color = "green"

    def newbtn2(self):
        self.btn2.background_color = "green"

    def newbtn3(self):
        self.btn3.background_color = "green"


# class for managing screens
class windowManager(ScreenManager):
    pass


# kv file
kv = Builder.load_file('login.kv')
sm = windowManager()

# reading all the data stored
users = pd.read_csv('login.csv')

# adding screens
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(logDataWindow(name='logdata'))
sm.add_widget(mainmenuWindow(name='mainmenu'))
sm.add_widget(PechoWindow(name='Pecho'))
sm.add_widget(EspaldaWindow(name='Espalda'))


# class that builds gui
class loginMain(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    loginMain().run()
