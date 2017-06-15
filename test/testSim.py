# tesSim.py
#
# Kasey French, May 28th 2017
# ***********************************************************

from src.force import *
from src.particle import *
from src.nBodySimulator import *
import matplotlib.pyplot as plt
import time 
import numpy as np

def test():

	p1 = MassParticle(1.989e30,
	                  State(pos = [.0, .0, .0]))

	p2 = MassParticle(5.972e24,
	                  State(pos = [1.496e11, 0.000e00, 0.000e00],
	                        vel = [0.000e00, 2.978e04, 0.000e00]))

	p3 = MassParticle(7.3477e22,
	                  State(pos = [1.496e11 + 3.844e08, 0.000e00, 0.000e00],
													vel = [0.000e00, 2.978e04 + 1.022e03, 0.000e00]))

	p4 = MassParticle(500,
	                   State(pos = [1.496e11 + 7.000e06, 0.000e00, 0.000e00],
													 vel = [0.000e00, 2.978e04 + 1.222e04, 5.500e03]))

	pList = [p1, p2, p3, p4]

	nMasses = 5
	meanPos = p2.state.pos
	stdPos = 8.0e08 * np.ones((3,1))
	meanVel = p2.state.vel
	stdVel = 1.e02 * np.ones((3,1))
	meanMass = 1.e22
	stdMass = 1.e21

	massFactory = MassFactory()
	massList = massFactory.generateRandomMasses(nMasses, meanPos, stdPos, 
	                                            meanVel, stdVel, meanMass, 
	                                            stdMass)

	massList.extend(pList)

	galaxy = Nbodysim(pList, Gravity)
	tspan = np.linspace(0,365*86400,7000)

	galaxy.integrate(tspan)

	########## Less accurate numerical approximation. #########
	########## massStates = galaxy.run(tspan) #########

	galaxy.plotSim3D()
  ########## Labels still need to be worked on. ##########
	labels = {id(p1.state) : "Sun" , id(p2.state) : "Earth" ,
	 					id(p3.state) : "Moon" , id(p4.state) : "Satellite"}

	#tlist = [id(a.state) for a in massList if id(a.state) != id(p1.state)]
	tlist = [id(p1.state), id(p3.state), id(p4.state)]

	galaxy.plotSim3D()
	galaxy.plotSim2D(labels)
	galaxy.plotSim2DRelative(tlist, id(p2.state),labels)
	galaxy.plotSim3DRelative(tlist, id(p2.state),labels)
	plt.show()

if __name__ == '__main__':
	test()



#EOF