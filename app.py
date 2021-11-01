from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout as gl



class MyApp(App):
    def build(self):  
        layout = gl(cols=2)
        btn1 = Button()
        btn2 = Button()
        btn3 = Button()
        btn4 = Button()

        btn5 = Button()
        layout.add_widget(btn5)
        layout.add_widget(btn4)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
            
        return layout


if  __name__ == "__main__":
    MyApp().run() 