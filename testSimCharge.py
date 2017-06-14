# tesSimCharge.py
#
# Kasey French, May 28th 2017
# ***********************************************************

from force import *
from particle import *
from nBodySimulator import *
import matplotlib.pyplot as plt
import time 
import numpy as np

electron = -1.0
proton = 1.0

def test():
	
	# Test charges are a proton and an electron in a hydrogen atom.
	# Add in charges mass to better approximate acceleration.

	testParticle1 = ChargedParticle(electron,State(pos = [1.0,.0,.0],\
	                                               vel = [.0,10.,.0]))
	testParticle2 = ChargedParticle(proton,State(pos = [.0,.0,.0]))

	testParticleList = [testParticle1, testParticle2]

	atom = Nbodysim(testParticleList, Electromagnetism)
	tspan = np.linspace(0,.1,500)
	atomStates = atom.run(tspan)

	atom.plotSim3D()

	atom.plotSim2D()

	plt.show()

if __name__ == '__main__':
	test()




#EOF