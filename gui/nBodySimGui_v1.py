""" nBodySimGui_v1.py


Kasey French, June 17th, 2017"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
from nbodysim import *
from matplotlib import pyplot as plt
import seaborn
import numpy as np

mainAppClass, baseClass = uic.loadUiType('nBodySimGui_v1.ui')

popUpClass, _ = uic.loadUiType('nbodysimPopup.ui')
popUpClass2, _ = uic.loadUiType('nbodysimPopup2.ui')

class myPopUp(popUpClass, baseClass):
	def __init__(self):
		super(myPopUp, self).__init__()
		self.setupUi(self)

		self.nParticleBox.setText('10')
		self.meanMassBox.setText('1.000e30')
		self.stdMassBox.setText('1.000e29')

		self.xmeanPosBox.setText('0.000e00')
		self.xstdPosBox.setText('1.000e13')
		self.xmeanVelBox.setText('0.000e00')
		self.xstdVelBox.setText('1.000e01')

		self.ymeanPosBox.setText('0.000e00')
		self.ystdPosBox.setText('1.000e13')
		self.ymeanVelBox.setText('0.000e00')
		self.ystdVelBox.setText('1.000e01')

		self.zmeanPosBox.setText('0.000e00')
		self.zstdPosBox.setText('1.000e13')
		self.zmeanVelBox.setText('0.000e00')
		self.zstdVelBox.setText('1.000e01')

		self.tspanBox.setText('1000')

	# def getValues(self):
	# 	self.mean

class myPopUp2(popUpClass2, baseClass):
	def __init__(self):
		super(myPopUp2, self).__init__()
		self.setupUi(self)

		self.massBox.setText('1.000e10')
		self.chargeBox.setText('0.000e00')

		self.xPosBox.setText('0.000e00')
		self.yPosBox.setText('0.000e00')
		self.zPosBox.setText('0.000e00')

		self.xVelBox.setText('0.000e00')
		self.yVelBox.setText('0.000e00')
		self.zVelBox.setText('0.000e00')

class myApp(mainAppClass, baseClass):
	def __init__(self):
		super(myApp, self).__init__()
		self.setupUi(self)
		self.myList = []
		self.labels = {}

		self.genParticleDistButton.clicked.connect(self.genPD)
		self.genSpecDistBut.clicked.connect(self.genSPD)
		self.movieBut.clicked.connect(self.createMovie)

	def genPD(self, item):
		self.w = myPopUp()
		self.w.show()
		self.w.enterButton.clicked.connect(self.testPlot)

	def genSPD(self, item):
		self.w2 = myPopUp2()
		self.createMovieBut = QPushButton(self.w2.frame)
		self.createMovieLabel = QLabel(self.w2.frame)
		self.createMovieBut.move(250,310)
		self.createMovieLabel.move(250,290)
		self.createMovieLabel.setText('Create Movie:')
		self.w2.show()
		self.myList = []
		self.labels.clear()
		self.w2.moreMassesBut.clicked.connect(self.addMasses)
		self.w2.simulateBut.clicked.connect(self.testPlot2)
		self.createMovieBut.clicked.connect(self.movieCreator)

	def createMovie(self, item):
		self.w2 = myPopUp2()
		self.nameBox = QLineEdit(self.w2.frame)
		self.nameLabel = QLabel(self.w2.frame)
		self.nameBox.move(250,310)
		self.nameLabel.move(250,290)
		self.nameLabel.setText('Filename:')
		self.frameBox = QLineEdit(self.w2.frame)
		self.frameLabel = QLabel(self.w2.frame)
		self.frameBox.move(250, 250)
		self.frameLabel.move(250,230)
		self.frameLabel.setText('Frames:')
		self.w2.show()
		self.myList = []
		self.labels.clear()
		self.w2.moreMassesBut.clicked.connect(self.addMasses)
		self.w2.simulateBut.clicked.connect(self.movieCreator)


	def testPlot(self, item):

		nBodies = int(self.w.nParticleBox.text())

		(xmeanPos, ymeanPos, zmeanPos) = (float(self.w.xmeanPosBox.text()),
																				float(self.w.ymeanPosBox.text()),
																				float(self.w.zmeanPosBox.text()))

		xstdPos, ystdPos, zstdPos = (float(self.w.xstdPosBox.text()),
																	float(self.w.ystdPosBox.text()),
																	float(self.w.zstdPosBox.text()))

		xmeanVel, ymeanVel, zmeanVel = (float(self.w.xmeanVelBox.text()),
																			float(self.w.ymeanVelBox.text()),
																			float(self.w.zmeanVelBox.text()))

		xstdVel, ystdVel, zstdVel = (float(self.w.xstdVelBox.text()),
																	float(self.w.ystdVelBox.text()),
																	float(self.w.zstdVelBox.text()))

		meanMass = float(self.w.meanMassBox.text())
		stdMass = float(self.w.stdMassBox.text())

		meanPos = reshape(np.array([xmeanPos, ymeanPos, zmeanPos]), (3,1))
		stdPos = reshape(np.array([xstdPos, ystdPos, zstdPos]), (3,1))
		meanVel = reshape(np.array([xmeanVel, ymeanVel, zmeanVel]), (3,1))
		stdVel = reshape(np.array([xstdVel, ystdVel, zstdVel]), (3,1))

		tspan = 86400.0 * float(self.w.tspanBox.text())
		tspan = np.linspace(0, tspan, 5000)

		myMassFactory = MassFactory()
		mList = myMassFactory.generateRandomMasses(nBodies, meanPos, stdPos,
																			 				meanVel, stdVel, meanMass,
																			 				stdMass)
		# x = [x.state.pos[0] for x in mList]
		# y = [y.state.pos[1] for y in mList]

		#plt.figure()
		#plt.plot(x,y,'.')

		myGrav = Gravity()
		self.simulator  = Nbodysim(mList, [myGrav])
		self.simulator.integrate(tspan)
		plt.figure()
		self.simulator.plotSim2D()
		self.simulator.plotSim3D()

		plt.show()
		self.w.close()

	def addMasses(self, item):

		mass = float(self.w2.massBox.text())
		charge = float(self.w2.chargeBox.text())
		(xPos, yPos, zPos) = (float(self.w2.xPosBox.text()),
													float(self.w2.yPosBox.text()),
													float(self.w2.zPosBox.text()))

		(xVel, yVel, zVel) = (float(self.w2.xVelBox.text()),
														float(self.w2.yVelBox.text()),
														float(self.w2.zVelBox.text()))

		pos = [xPos, yPos, zPos]
		vel = [xVel, yVel, zVel]

		dummyParticle = ChargedMass(mass, charge, state =
		                		State(pos = pos, vel = vel))

		self.myList.append(dummyParticle)
		label = str(self.w2.labelBox.text())
		if label != None:
			newLabels = {id(dummyParticle.state) : label}
			self.labels.update(newLabels)

		nSpaces = -(len(label) - 20)
		self.w2.massList.addItem(label + (' ' * nSpaces) + str(dummyParticle.mass)
		                         + '    ' + str(dummyParticle.state.pos[0])
		                         + '  ' + str(dummyParticle.state.pos[1])
		                         + '  ' + str(dummyParticle.state.pos[2])
		                         + '    ' + str(dummyParticle.state.vel[0])
		                         + '  ' + str(dummyParticle.state.vel[1])
		                         + '  ' + str(dummyParticle.state.vel[2]))

		self.w2.massBox.setText('1.000e10')
		self.w2.chargeBox.setText('0.000e00')
		self.w2.labelBox.clear()

		self.w2.xPosBox.setText('0.000e00')
		self.w2.yPosBox.setText('0.000e00')
		self.w2.zPosBox.setText('0.000e00')

		self.w2.xVelBox.setText('0.000e00')
		self.w2.yVelBox.setText('0.000e00')
		self.w2.zVelBox.setText('0.000e00')

	def testPlot2(self, item):
		tspan = 86400.0 * float(self.w2.tSpanBox.text())
		tspan = np.linspace(0, tspan, 5000)
		myGrav  = Gravity()
		myElectro = Electromagnetism()

		plt.figure()
		self.mySystem = Nbodysim(self.myList, [myGrav, myElectro])
		self.mySystem.integrate(tspan)
		self.mySystem.plotSim2D(labels = self.labels)
		self.myList = []
		self.labels.clear()
		self.w2.massList.clear()
		self.w2.tSpanBox.clear()

		plt.legend()
		plt.show()

	def movieCreator(self,item):

		tspan = 86400.0 * float(self.w2.tSpanBox.text())
		tspan = np.linspace(0, tspan, 2000)
		myGrav  = Gravity()
		myElectro = Electromagnetism()

		self.mySystem = Nbodysim(self.myList, [myGrav, myElectro])
		print 'Integrating...'
		self.mySystem.integrate(tspan)
		x = [abs(p[0]) for _,pList in self.mySystem.particleStates.iteritems() for p in pList]
		y = [abs(p[1]) for _,pList in self.mySystem.particleStates.iteritems() for p in pList]

		xlim = 1.5 * max(x)
		ylim = 1.5 * max(y)

		name = str(self.nameBox.text())
		self.mySystem.animate2D(xlim = [-xlim, xlim],
		                         	ylim = [-ylim, ylim],
		                         	filename = name,
		                         	nframes = int(self.frameBox.text()),
		                         	labels = self.labels)
		print 'File created'
		self.myList = []
		self.labels.clear()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = myApp()
	main.show()
	app.exec_()




# EOF