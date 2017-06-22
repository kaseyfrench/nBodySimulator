""" HelloWorld.py


Kasey French, June 17th, 2017"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

formClass, baseClass = uic.loadUiType('HelloWorld.ui')

class myApp(formClass, baseClass):
	def __init__(self):
		super(myApp, self).__init__()

		self.setupUi(self)

		self.helloWorldButton.clicked.connect(self.helloworld)

	def helloworld(self, item):
		print('hi')




if __name__ =='__main__':
	app = QApplication(sys.argv)
	main = myApp()
	main.show()
	app.exec_()

# EOF