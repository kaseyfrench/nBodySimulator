# tesSim.py
#
# Kasey French, May 28th 2017
# ***********************************************************

from force import *
from particle import *
from nBodySimulator import *
import matplotlib.pyplot as plt
import time 
import numpy as np

def test():
	# m1 = MassParticle(60., State(pos = [6.378e6,0.,0.]))
	# m2 = MassParticle(5.972e24)

	# m3 = MassParticle(1.898e27, State(pos = [3.84e8,0.,0.]))

	# grav = Gravity()

	# accMass = grav.computeAccel(m1,[m2,m3])

	# electroncharge = -1.602e-19
	# protoncharge = 1.602e-19

	# c1 = ChargedParticle(electroncharge, State(pos = [53.e-12,0.,0.]))
	# c2 = ChargedParticle(protoncharge, State(pos = [0.,0.,0.]))

	# electro = Electromagnetism()

	# accElectro = electro.computeAccel(c1,[c2]) 

	# print accMass
	# print '\n'
	# print accElectro
	testParticle1 = MassParticle(1.989e30,State(pos = [.0,.0,.0]))
	testParticle2 = MassParticle(5.972e24,State(pos = [1.496e11,0.,0.],\
	                                        vel = [.0,2.978e4,.0]))
	testParticle3 = MassParticle(7.3477e22,State(pos = [1.496e11+3.844e8,.0,.0],\
																					vel = [.0,2.978e4+1.022e3,.0]))
	testParticle4 = MassParticle(500,State(pos = [1.496e11+7e6,0.,.0],\
																					 vel = [.0,2.978e4+1.222e4,5.5e3]))

	testList = [testParticle1, testParticle2, testParticle3, testParticle4]

	massFactory = MassFactory()
	massList = massFactory.generateRandomMasses(5,testParticle2.state.pos,\
	       np.ones((3,1))*8.e8,testParticle2.state.vel,np.ones((3,1))*1.e2,1.e22,1.e21)

	#for massparticle in testList:
	#	massparticle.state.display()
	massList.extend(testList)

	galaxy = Nbodysim(testList, Gravity)
	tspan = np.linspace(0,365*86400,7000)

	galaxy.integrate(tspan)

	# massStates = galaxy.run(tspan)

	#for massparticle in testList:
	#	massparticle.state.display()

	# galaxy.plotSim3D()

	labels = {id(testParticle1.state) : "Sun" , id(testParticle2.state) : "Earth" ,\
	 id(testParticle3.state) : "Moon" , id(testParticle4.state) : "Satellite"}

	#tlist = [id(a.state) for a in massList if id(a.state) != id(testParticle1.state)]
	tlist = [id(testParticle1.state), id(testParticle3.state), id(testParticle4.state)]
	
	galaxy.plotSim2D(labels)
	galaxy.plotSim2DRelative(tlist, id(testParticle2.state),labels)
	galaxy.plotSim3DRelative(tlist, id(testParticle2.state),labels)
	plt.show()

if __name__ == '__main__':
	test()



#EOF