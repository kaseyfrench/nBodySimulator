# testMultipleForce.py
#
#
# Kasey French, June 16th 2017

from nbodysim import *
import numpy as np
import matplotlib.pyplot as plt

def test():

	chargedMass1 = ChargedMass(1.989e30, 3.400e17)
	chargedMass2 = ChargedMass(5.972e24, 2.500e17,
	               	State(pos = [1.496e11, 0.000e00, 0.000e00],
	               	      vel = [0.000e00, 2.978e03, 0.000e00]))

	mass1 = MassParticle(1.989e30)
	mass2 = MassParticle(5.972e24,
	        State(pos = [1.496e11, 0.000e00, 0.000e00],
	              vel = [0.000e00, 2.978e04, 0.000e00]))

	tspan = np.linspace(0, 365 * 5 * 86400, 4000)

	plt.figure(1)
	plt.axis('equal')

	myGrav = Gravity()
	myElectro = Electromagnetism()

	test1 = Nbodysim([chargedMass1, chargedMass2], [myGrav, myElectro])
	test1.integrate(tspan)
	test1.plotSim2D()

	plt.figure(2)
	plt.axis('equal')

	test2 = Nbodysim([mass1, mass2], [myGrav])
	test2.integrate(tspan)
	test2.plotSim2D()

	plt.show()

if __name__ == '__main__':
	test()




#EOF