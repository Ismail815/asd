import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from urllib3.util.wait import select_wait_for_socket


class MyGrid(GridLayout):
    def __init__ (self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="İsim: "))
        self.isim = TextInput(multiline=False)
        self.add_widget(self.isim)

        self.add_widget(Label(text="Soyisim: "))
        self.soyisim = TextInput(multiline=False)
        self.add_widget(self.soyisim)

        self.add_widget(Label(text="Yas: "))
        self.yas = TextInput(multiline=False)
        self.add_widget(self.yas)

        self.add_widget(Label(text="Mail: "))
        self.mail = TextInput(multiline=False)
        self.add_widget(self.mail)


class tt(App):
    def build(self):
        return MyGrid()
if __name__ == "__main__":
    tt().run()