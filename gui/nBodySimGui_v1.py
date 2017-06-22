""" nBodySimGui_v1.py


Kasey French, June 17th, 2017"""

try:
	from PyQt4.QtGui import *
	from PyQt4.QtCore import *
	from PyQt4 import uic
except:
	try:
		from PyQt5.QtGui import *
		from PyQt5.QtCore import *
		from PyQt5 import uic
		from PyQt5.QtWidgets import *
	except:
		raise ImportError('nBodySim requires PyQt4 or PyQt5')

import sys
from nbodysim import *
from matplotlib import pyplot as plt
import numpy as np

plt.style.use(['dark_background'])
myGrav = Gravity()

mainAppClass, baseClass = uic.loadUiType('nBodySimGui_v1.ui')

popUpClass, _ = uic.loadUiType('nbodysimPopup.ui')
popUpClass2, _ = uic.loadUiType('nbodysimPopup2.ui')

class myPopUp(popUpClass, baseClass):
	def __init__(self):
		super(myPopUp, self).__init__()
		self.setupUi(self)

		self.nParticleBox.setText('10')
		self.meanMassBox.setText('1.000e32')
		self.stdMassBox.setText('1.000e31')

		self.xmeanPosBox.setText('0.000e00')
		self.xstdPosBox.setText('1.000e13')
		self.xmeanVelBox.setText('0.000e00')
		self.xstdVelBox.setText('1.000e04')

		self.ymeanPosBox.setText('0.000e00')
		self.ystdPosBox.setText('1.000e13')
		self.ymeanVelBox.setText('0.000e00')
		self.ystdVelBox.setText('1.000e04')

		self.zmeanPosBox.setText('0.000e00')
		self.zstdPosBox.setText('1.000e13')
		self.zmeanVelBox.setText('0.000e00')
		self.zstdVelBox.setText('1.000e04')

		self.tspanBox.setText('1000')

		#self.massTable.setRowCount(1)
		#self.massTable.setColumnCount(5)

	# def getValues(self):
	# 	self.mean

class myPopUp2(popUpClass2, baseClass):
	def __init__(self):
		super(myPopUp2, self).__init__()
		self.setupUi(self)

		self.massBox.setText('1.970e30')
		self.chargeBox.setText('0.000e00')

		self.labelBox.setText('Sun')

		self.xPosBox.setText('0.000e00')
		self.yPosBox.setText('0.000e00')
		self.zPosBox.setText('0.000e00')

		self.xVelBox.setText('0.000e00')
		self.yVelBox.setText('0.000e00')
		self.zVelBox.setText('0.000e00')

		self.tSpanBox.setText('365')
		self.nFramesBox.setText('365')
		self.bitRateBox.setText('1800')
		self.fpsBox.setText('30')

		self.outFileBox.setText('nbodysim.anim')


class myApp(mainAppClass, baseClass):
	def __init__(self):
		super(myApp, self).__init__()
		self.setupUi(self)
		self.myList = []
		self.labels = {}

		self.genParticleDistButton.clicked.connect(self.genPD)
		self.genSpecDistBut.clicked.connect(self.genSPD)
		self.quickPlotBut.clicked.connect(self.quickPlot)
		self.orbitingSystemBut.clicked.connect(self.orbitingSystem)
		self.collidingSystemBut.clicked.connect(self.collidingSystem)

	def genPD(self, item):
		self.w = myPopUp()
		self.w.show()
		self.w.enterButton.clicked.connect(self.testPlot)

	def genSPD(self, item):
		self.w2 = myPopUp2()
		self.w2.show()
		self.myList = []
		self.labels.clear()
		self.w2.massTable.clear()
		self.w2.tSpanBox.setText('365')
		self.w2.moreMassesBut.clicked.connect(self.addMasses)
		self.w2.simulateBut.clicked.connect(self.movieCreator)
		# self.createMovieBut.clicked.connect(self.movieCreator)

	def quickPlot(self, item):
		self.w2 = myPopUp2()
		self.w2.show()
		self.myList = []
		self.labels.clear()
		self.w2.moreMassesBut.clicked.connect(self.addMasses)
		self.w2.simulateBut.clicked.connect(self.testPlot2)


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

		# nSpaces = -(len(label) - 20)
		# self.w2.massList.addItem(label + (' ' * nSpaces) + str(dummyParticle.mass)
		#                          + '    ' + str(dummyParticle.state.pos[0])
		#                          + '  ' + str(dummyParticle.state.pos[1])
		#                          + '  ' + str(dummyParticle.state.pos[2])
		#                          + '    ' + str(dummyParticle.state.vel[0])
		#                          + '  ' + str(dummyParticle.state.vel[1])
		#                          + '  ' + str(dummyParticle.state.vel[2]))

		mass = '{0:g}'.format(dummyParticle.mass)
		chrg = '{0:g}'.format(dummyParticle.charge)
		rmag = '{0:g}'.format(np.linalg.norm(dummyParticle.state.pos))
		vmag = '{0:g}'.format(np.linalg.norm(dummyParticle.state.vel))

		row = self.w2.massTable.rowCount() - 1
		self.w2.massTable.setItem(row, 0, QTableWidgetItem(label))
		self.w2.massTable.setItem(row, 1, QTableWidgetItem(mass))
		self.w2.massTable.setItem(row, 2, QTableWidgetItem(chrg))
		self.w2.massTable.setItem(row, 3, QTableWidgetItem(rmag))
		self.w2.massTable.setItem(row, 4, QTableWidgetItem(vmag))
		self.w2.massTable.insertRow(row+1)

		self.w2.massBox.setText('5.970e24')
		self.w2.chargeBox.setText('0.000e00')
		self.w2.labelBox.clear()

		self.w2.xPosBox.setText('1.490e11')
		self.w2.yPosBox.setText('0.000e00')
		self.w2.zPosBox.setText('0.000e00')

		self.w2.xVelBox.setText('0.000e00')
		self.w2.yVelBox.setText('2.970e04')
		self.w2.zVelBox.setText('0.000e00')

		self.w2.labelBox.setText('Earth')

	def testPlot2(self, item):
		tspan = 86400.0 * float(self.w2.tSpanBox.text())
		tspan = np.linspace(0, tspan, 5000)
		myElectro = Electromagnetism()

		plt.figure()
		self.mySystem = Nbodysim(self.myList, [myGrav, myElectro])
		self.mySystem.integrate(tspan)
		self.mySystem.plotSim2D(labels = self.labels)

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

		name = str(self.w2.outFileBox.text())
		self.mySystem.animate2D(xlim = [-xlim, xlim],
		                         	ylim = [-ylim, ylim],
		                         	filename = name,
		                         	nframes = int(self.w2.nFramesBox.text()),
		                         	labels = self.labels)
		print 'File created'

	def orbitingSystem(self, item):

		mySystem = orbitingSystemClass()

		self.orbitingSim = Nbodysim(mySystem.getList(), [myGrav])
		tspan = 86400.0 * 10000
		tspan = np.linspace(0, tspan, 2000)
		self.orbitingSim.integrate(tspan)
		self.orbitingSim.plotSim2D()

		plt.show()

	def collidingSystem(self, item):

		firstSystem = orbitingSystemClass()
		secondSystem = orbitingSystemClass()
		thirdSystem = orbitingSystemClass()
		fourthSystem = orbitingSystemClass()
		bodies1 = firstSystem.getList()
		bodies2 = secondSystem.getList()
		bodies3 = thirdSystem.getList()
		bodies4 = fourthSystem.getList()

		for k in bodies1:
			k.state.pos[0] += 5.000e012
			k.state.vel[1] += 0.000e03
			#k.state.vel[0] -= 1.000e03

		for k in bodies2:
			k.state.pos[0] -= 5.000e12
			k.state.vel[1] -= 2.000e03
			#k.state.vel[0] += 1.000e03

		# for k in bodies3:
		# 	k.state.pos[1] -= 6.000e12
		# 	k.state.vel[0] += 2.000e04

		# for k in bodies4:
		# 	k.state.pos[1] += 6.000e12
		# 	k.state.vel[0] -= 2.000e04

		List = bodies1 + bodies2
		mySimulator = Nbodysim(List, [myGrav])

		tspan = 86400.0 * 100000
		tspan = np.linspace(0, tspan, 3000)
		print 'Integrating...'
		mySimulator.integrate(tspan)
		x = [abs(p[0]) for _,pList in mySimulator.particleStates.iteritems() for p in pList]
		y = [abs(p[1]) for _,pList in mySimulator.particleStates.iteritems() for p in pList]

		xlim = 1.5 * max(x)
		ylim = 1.5 * max(y)
		print 'Animating...'
		mySimulator.animate2D(xlim = [-xlim, xlim],
		                         	ylim = [-ylim, ylim],
		                         	filename = 'testCollision',
		                         	nframes = 1000,
		                         	labels = {})

class orbitingSystemClass(object):

	def __init__(self):
		self.bodies = []
		self.centerBody = MassParticle(1.000e31 + 1.000e30 * np.random.standard_normal((1,1)),
		                               State(pos = [0, 0, 0] + np.random.standard_normal((1,1)) * 1.000e01))

		G = 6.674e-11

		n = np.random.randint(low = 1, high = 9)
		for x in range(1,n):
			self.bodies.append(MassParticle(1.000e25 + 5.000e23 * np.random.standard_normal((1,1)),
			               	State(pos = np.random.standard_normal((3,1)) * 9.000e11)))


		M = self.centerBody.mass + sum(particle.mass for particle in self.bodies)

		for particle in self.bodies:
			particle.state.pos[2] = 0
			particle.state.vel = np.cross(np.reshape(particle.state.pos, (1,3)), [0, 0, 1], axisc = 0)
			particle.state.vel = particle.state.vel / np.linalg.norm(particle.state.vel)
			particle.state.vel = np.sqrt(G * M / np.linalg.norm(particle.state.pos)) * particle.state.vel

		self.bodies.append(self.centerBody)

	def getList(self):
		return self.bodies







if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = myApp()
	main.show()
	app.exec_()




# EOF