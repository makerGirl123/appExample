from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

#used to set screen size
from kivy.core.window import Window

#example Android screen size
Window.size = (412, 896)


class AboutMeApp(MDApp):
    def build(self):
        #Light Mode
        #self.theme_cls.primary_palette = "Blue"
        #self.theme_cls.primary_hue = "A700"
        #self.theme_cls.theme_style = "Light"

        #Dark Mode
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

        #Create the screen object
        #screen = Screen()

        #Create a button
        #btn_flat = MDRectangleFlatButton(text='Hello World', pos_hint={'center_x':0.5, 'center_y':0.5})


        #Create a Label
        #label = MDLabel(text="All About Me", pos_hint={'center_x':0.5, 'center_y':0.8}, theme_text_color="Secondary", font_style="H2")

        #If Declarative: Adding widgets to the screen
        #screen.add_widget(label)
        #screen.add_widget(btn_flat)






if __name__ == '__main__':
    AboutMeApp().run()