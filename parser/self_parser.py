from bs4 import BeautifulSoup
import requests, fake_useragent
import webbrowser
import os
from pdf2image import convert_from_path
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.image import Image
from kivy.config import Config 

Config.set('graphics', 'resizable', True)

groups = [
		  #1 курс
		  "901а","901б","901в","901с1","901с2",
		  "903а1","903а2","903б1","903б2","903в",
		  "907а1","907а2","907б1","907б2","907в1","907в2","907г1","907г2",
		  "907са1","907са2","907сб1","907сб2","907св1","907св2",
		  #2 курс
		  "801а1","801а2","801б2","801в1","801в2","801с1","801с2",
		  "803а1","803а2","803б1","803б2","803в1","803в2","803г1","803г2","803е1","803е2",
		  "803з1","803з2","803са1","803са2","803сб1",
		  "807са2",
		  #3 курс
		  "701а1","701а2","701с",
		  "703а","703а2","703б1","703б2","703в1","703в2","703г1","703г2","703са1","703са2",
		  #4 курс
		  "603а1","603а2"]
cur_group = ''
sm = ScreenManager()
kv = Builder.load_file("parser.kv")

class GroupButton(Button):
	def GoToGroupPage(self):
		global cur_group
		cur_group = self.text
		sm.switch_to(GroupWindow(), direction = 'up')

class RV(RecycleView):
	def __init__(self, **kwargs):
		super(RV, self).__init__(**kwargs)
		self.data = [{'text': x} for x in groups]

class MainWindow(Screen):
	def GoToSelectionPage(self):
		sm.switch_to(SelectionWindow(),direction = "left")

class SelectionWindow(Screen):
	def GoToMainPage(self):
		sm.switch_to(MainWindow(), direction = "right")
		
class GroupWindow(Screen):
	GroupName = StringProperty()
	def __init__(self, **kwargs):
		super(GroupWindow, self).__init__()
		global cur_group
		self.GroupName = cur_group
	def GoToSelectionPage(self):
		sm.switch_to(SelectionWindow(),direction = "down")
	def GoToConstSchedule(self):
		pass
		'''ua = fake_useragent.UserAgent() 
		user = ua.random
		header = {'User-Agent':str(user)}
		# Parse site
		global cur_group
		if cur_group[0] == '9':
			if cur_group[3] == 'с':
				name = "Основное расписание 1 курса СПО"
			else:
				name = "Основное расписание 1 курса БО"
		elif cur_group[0] == '8':
			if cur_group[3] == 'с':
				name = "Основное расписание 2 курса СПО"
			else:
				name = "Основное расписание 2 курса БО"
		elif cur_group[0] == '7':
			if cur_group[3] == 'с':
				name = "Основное расписание 3,4 курса СПО"
			else:
				name = "Основное расписание 3 курса СПО"
		elif cur_group[0] == '6':
			name = "Основное расписание 3,4 курса СПО"
		url = 'ci.nsu.ru/education/schedule/'
		page = requests.get("http://"+url.split()[0], headers = header)
		soup = BeautifulSoup(page.text, "html.parser")
		i=0
		for tag in soup.findAll('a'):
			if name in tag.text:
				url = "https://ci.nsu.ru"+tag['href']'''
	def GoToConstSchedule(self):
		ua = fake_useragent.UserAgent() 
		user = ua.random
		header = {'User-Agent':str(user)}
		# Parse site
		global cur_group
		if cur_group[0] == '9':
			if cur_group[3] == 'с':
				name = "Основное расписание 1 курса СПО"
			else:
				name = "Основное расписание 1 курса БО"
		elif cur_group[0] == '8':
			if cur_group[3] == 'с':
				name = "Основное расписание 2 курса СПО"
			else:
				name = "Основное расписание 2 курса БО"
		elif cur_group[0] == '7':
			if cur_group[3] == 'с':
				name = "Основное расписание 3,4 курса СПО"
			else:
				name = "Основное расписание 3 курса СПО"
		elif cur_group[0] == '6':
			name = "Основное расписание 3,4 курса СПО"
		url = 'ci.nsu.ru/education/schedule/'
		page = requests.get("http://"+url.split()[0], headers = header)
		soup = BeautifulSoup(page.text, "html.parser")
		i=0
		for tag in soup.findAll('a'):
			if name in tag.text:
				url = "https://ci.nsu.ru"+tag['href']
				#r = requests.get(url, stream=True)
				webbrowser.open(url,new = 2)
				#path=os.getcwd()
				'''with open('newpdf.pdf','wb') as f:
					f.write(r.content)
				pages = convert_from_path('newpdf.pdf')
				for p in pages:
					p.save('out{}.jpg'.format(i),'JPEG')
					i+=1'''
				#os.remove('newpdf.pdf')
		#img_0 = Image(source = 'out0.jpg')
		#img_1 = Image(source = 'out1.jpg',size = self.texture_size)

		#bl.add_widget(img_0)
		#bl.add_widget(img_1)

		#os.remove('out0.jpg')
		#os.remove('out1.jpg')
		#sm.switch_to(ConstScheduleWindow(),direction = "right")

class ConstScheduleWindow(Screen):
	img_0 = StringProperty()
	img_1 = StringProperty()
	def __init__(self, **kwargs):
		super(ConstScheduleWindow, self).__init__()
		img_0 = 'out0.jpg'
		img_1 = 'out1.jpg'
	def GoToGroupPage(self):
		sm.switch_to(GroupWindow(), direction = 'left')

class ParseApp(App):
	def build(self):
		global sm
		mainScreen = MainWindow(name = 'main')
		selectionScreen = SelectionWindow(name = 'selection')
		groupScreen = GroupWindow(name = 'group')
		constScheduleScreen = ConstScheduleWindow(name = 'constSchedule')
		sm.add_widget(mainScreen)
		sm.add_widget(selectionScreen)
		sm.add_widget(groupScreen)
		sm.add_widget(constScheduleScreen)
		return sm

if __name__ == "__main__":
	ParseApp().run()

# Random User-Agent
'''ua = fake_useragent.UserAgent() 
user = ua.random
header = {'User-Agent':str(user)}

# Parse site
url = 'ci.nsu.ru/education/schedule/'

cl = input('Enret grade:\n')
name = "Основное расписание "+cl+" курса СПО"
	
page = requests.get("http://"+url.split()[0], headers = header)

soup = BeautifulSoup(page.text, "html.parser")

for tag in soup.findAll('a'):
	if name in tag.text:
		print(tag['href'])
		webbrowser.open_new("https://ci.nsu.ru"+tag['href'])'''
		
# Default parse - HTML 
'''if url.split()[0] == url.split()[-1]:
	with open("index.html","w") as html:
		for tag in soup.findAll('html'):
			html.write(str(tag))
		print("\nFile: 'index.html' created")
else:
	# Parse tag
	if url.split()[1] == url.split()[-1]:
		for tag in soup.findAll(url.split()[1]):
			print(tag)
	# Parse inside/attribute
	else:
		if url.split()[2] == "inside":
			for tag in soup.findAll(url.split()[1]):
				print(tag.text)
		else:
			for tag in soup.findAll(url.split()[1]):
				print(tag[url.split()[2]])'''