from kivy.tests.common import GraphicUnitTest
import unittest
import pandas as pd
import pytest


class Pruebas(unittest.TestCase):
    # btn = ObjectProperty(None)

    def test_validate(self):

        # validating if the email already exists
        users = pd.read_csv('login.csv')
        if "santiago@gmail.com" not in users['Email'].unique():
            result = 0
        else:
            result = 1
        self.assertEqual(result, 1)

    def test_signupbtn(self):
        # creating a DataFrame of the info
        users = pd.read_csv('login.csv')
        user = pd.DataFrame([["Adolfo", "adolfo@gmail.com", "123"]],
                            columns=['Name', 'Email', 'Password'])
        if "adolfo@gmail.com" not in users['Email'].unique():
            # if email does not exist already then append to the csv file
            user.to_csv('login.csv', mode='a', header=False, index=False)
            result = 1
        else:
            result = 0
        self.assertEqual(result, 1)


class Botones(GraphicUnitTest):
    def test_greenButton(self):
        from kivy.uix.button import Button
        button = Button(text="Press de banco incllinado", size_hint=(0.3, 0.1))
        self.render(button)

        button.bind(on_release=self.callback)

    def callback(self):
        self.background_color = "green"
        if self.background_color == "green":
            result = 1
        else:
            result = 0
        self.assertEqual(result, 1)

