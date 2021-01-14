'''
wdSync v0.0 by Klykov Leonid
Программа для отправки со стендов на сервер файлов с результатами испытаний
Development started 2020/12/30
Спасибо за идею AterCattus`у, его пост от 25 марта 2012 в 14:51 https://habr.com/ru/post/140649/
'''

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
	def on_created(self, event):
		print(event)

	def on_deleted(self, event):
		print(event)

	def on_moved(self, event):
		print(event)

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
