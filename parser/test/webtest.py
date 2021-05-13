from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.scrollview import ScrollView
from kivy.config import Config 
from pdf2image import convert_from_path
from PIL import Image
import sys

Config.set('graphics', 'resizable', 1)
kv = Builder.load_file('Test.kv')
sm = ScreenManager() 

class MainScreen(Screen):
    def go_to_second(self):

        #vertical
        '''img_0 = Image.open("out0.jpg")
        img_1 = Image.open("out1.jpg")
        w0, h0 = img_0.size
        w1, h1 = img_1.size
        img_0 = img_0.crop((45, 35, w0-1078, h0-340))
        img_1 = img_1.crop((52, 55, w1-1074, h1-352))
        images = [img_0,img_1]
        widths, heights = zip(*(i.size for i in images))
        total_height = sum(heights)
        max_width = max(widths)
        new_im = Image.new('RGB', (max_width, total_height))
        y_offset = 0
        for im in images:
            new_im.paste(im, (0, y_offset))
            y_offset += im.height
        new_im.save('out.jpg')'''

        #horizontal
        '''img_0 = Image.open("out0.jpg")
        img_1 = Image.open("out1.jpg")
        w0, h0 = img_0.size
        w1, h1 = img_1.size
        img_0 = img_0.crop((45, 35, w0-1078, h0-340))
        img_1 = img_1.crop((51, 58, w1-1092, h1-318))
        images = [img_0,img_1]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width,max_height))
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        new_im.save('out.jpg')'''

        sm.switch_to(second_screen, direction = 'left')

class SecondScreen(Screen):
    def go_to_main(self):
        sm.switch_to(main_screen, direction = 'right')

main_screen = MainScreen(name = 'main')
second_screen = SecondScreen(name = 'second')
sm.add_widget(main_screen)
sm.add_widget(second_screen)

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()