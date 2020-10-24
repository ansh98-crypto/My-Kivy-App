from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import socket
import select
import errno
import sys
import os
import subprocess
from threading import Thread

class socket_func:
    def __init__(self):
        self.socket = socket.socket()
        self.host = '192.168.1.3'
        self.port = 9999
        self.socket.connect((self.host, self.port))

    def recv_message(self):
            return str(self.socket.recv(120002).decode("utf-8"))


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Message: '))
        self.stats = TextInput(multiline=False)
        self.inside.add_widget(self.stats)
        self.add_widget(self.inside)

        self.enter = Button(text='Start Connection', font_size=10)
        self.enter.bind(on_press=self.establish_connection)
        self.add_widget(self.enter)

    def establish_connection(self, button):
        self.socket = socket_func()
        Thread(target=self.recv_message2).start()
        
    def recv_message2(self):
        while True:
            self.stats.text = self.socket.recv_message()


class Myapp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    Myapp().run()
