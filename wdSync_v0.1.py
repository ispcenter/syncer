'''
wdSync v0.1 by Klykov Leonid
Программа для отправки со стендов на сервер файлов с результатами испытаний
Development started 2020/12/30
Спасибо за идею AterCattus`у, его пост от 25 марта 2012 в 14:51 https://habr.com/ru/post/140649/
'''

#0 Imports
from time import sleep
from shutil import copyfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#1 Classes and functions

def sync(event):
	try:
		copyfile(sm to sm)
		print('Синхронизация проведена успешно')
	except IOError:
		print('Копирование не удалось')

class StendMode:
	'selecting settings for individual stend'
	def __init__(self, stendNetName, serverFolder):
		self.stendNetName = stendNetName
		self.serverFolder = serverFolder

class Handler(FileSystemEventHandler):
	def on_created(self, event):
		print(event)

	def on_deleted(self, event):
		print(event)

	def on_moved(self, event):
		print(event)

#2 ====== Preparing =========

#2.1 Define stend number
stendNetName = 'arm_0' #os.environ['COMPUTERNAME']

#2.2 get settings
if stendNetName == 'arm_0': sm = StendMode('arm_0', 'Arm_0')
if stendNetName == 'arm_1': sm = StendMode('arm_1', 'Arm_1')
if stendNetName == 'arm_2': sm = StendMode('arm_2', 'Arm_2')
if stendNetName == 'arm_3': sm = StendMode('arm_3', 'Arm_3')
if stendNetName == 'arm_5': sm = StendMode('arm_5', 'Arm_5')


#4 Launching program
observer = Observer()
observer.schedule(Handler(), path=r'D:\coded\maket_sinc', recursive=True)
observer.start()


try:
	while True:
		time.sleep(0.1)
except KeyboardInterrupt:
	observer.stop()

observer.join()

print('stopped')
input()