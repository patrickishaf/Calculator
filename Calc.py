from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class RootWid(BoxLayout):
    screen = ObjectProperty()
    screen2 = ObjectProperty()

    def clear_display(self):
        self.screen.text = ''
        self.screen2.text = ''

    def delete_char(self):
        length = len(self.screen.text)
        last_char = length - 1
        self.screen.text = self.screen.text[0:last_char]

    def add_char(self, buttonText):
        self.screen.text += buttonText

    def compute(self):
        try:
            expression = eval(self.screen.text)
            literal = str(expression)
            self.screen2.text = literal
        except ZeroDivisionError:
            self.screen2.text = 'infinity'
        except SyntaxError:
            self.screen2.text = '[color=ff0000]Syntax error[/color]'


class CalculatorApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls.theme_style = 'Dark'
        super().__init__(**kwargs)

    def build(self):
        return RootWid()


if __name__ == '__main__':
    CalculatorApp().run()
