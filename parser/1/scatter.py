from kivy.uix.scatter import Scatter
from kivy.app import App


class MyScatter(Scatter):
	pass


class ScatterApp(App):
	def build(self):
		s = MyScatter(size=(400, 400), size_hint=(None, None))
		s.top = 500
		#s.center_x = 600
		#s.center_y = 350
		return s


ScatterApp().run()