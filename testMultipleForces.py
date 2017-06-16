# testMultipleForce.py
#
#
# Kasey French, June 16th 2017

from src.force import *
from src.particle import *
from src.nBodySimulator import *
import numpy as np
import matplotlib.pyplot as plt

def test():

	chargedMass1 = ChargedMass(1.989e30, 1.000e18)
	chargedMass2 = ChargedMass(5.972e24, -1.000e18, 
	               	State(pos = [1.496e11, 0.000e00, 0.000e00],
	               	      vel = [0.000e00, 2.978e04, 0.000e00]))

	mass1 = MassParticle(1.989e30)
	mass2 = MassParticle(5.972e24, 
	        State(pos = [1.496e11, 0.000e00, 0.000e00],
	              vel = [0.000e00, 2.978e04, 0.000e00]))

	tspan = np.linspace(0, 365 * 5 * 86400, 4000)

	plt.figure(1)
	plt.axis('equal')

	test1 = Nbodysim([chargedMass1, chargedMass2], Gravity, Electromagnetism)
	test1.integrate(tspan)
	test1.plotSim2D()

	plt.figure(2)
	plt.axis('equal')

	test2 = Nbodysim([mass1, mass2], Gravity)
	test2.integrate(tspan)
	test2.plotSim2D()

	plt.show()

if __name__ == '__main__':
	test()




#EOF