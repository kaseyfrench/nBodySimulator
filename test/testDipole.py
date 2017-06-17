# testCME.py
#
#
# Kasey French, June 16th 2017

from nbodysim import *
import numpy as np
import matplotlib.pyplot as plt
from copy import copy

def test():

	Sun = ChargedMass(1.989e30)
	Earth = ChargedMass(5.972e24, state =
					 State(pos = [1.496e11, 0.000e00, 0.000e00],
	            	 vel = [0.000e00, 2.978e04, 0.000e00]))

	CMEpos = [6.957e09, 0.000e00, 0.000e00]
	CMEvel = [4.890e05, 3.050e04, 0.000e00]

	particles = ChargedMassFactory()

	CME = particles.generateRandomChargedMasses(5, CMEpos, 5.000e08 * np.ones((3,1)),
	                                      		CMEvel, 8.000e01 * np.ones((3,1)),
	                                      		(1.600e12 / 5), 1.000e11, 1.000e4, 2.000e03)
																						#Average CME mass, vel
	CME.append(Sun)
	CME.append(Earth)

	northPoleState = State(pos = [0.000e00, 0.000e00, 6.000e6])
	NorthPole = ChargedMass(0.000e00, 5.000e17, northPoleState)

	southPoleState = State(pos = [0.000e00, 0.000e00, -6.000e6])
	SouthPole = ChargedMass(0.000e00, -5.000e17, southPoleState)

	fixedCharges = {NorthPole : {'Particle' : Earth, 'State' : copy(northPoleState)},
								  SouthPole : {'Particle' : Earth, 'State' : copy(southPoleState)}}


	labels = {id(Sun.state) : "Sun", id(Earth.state) : "Earth"}

	myGrav = Gravity()
	myElectro = Electromagnetism()

	mySystem = Nbodyfixedcharges(CME, [myGrav, myElectro], fixedCharges)

	tspan = np.linspace(0, 3.7 * 86400, 4000)
	mySystem.integrate(tspan)
	plt.figure(1)
	mySystem.plotSim2D(labels) # Why don't the labels show?
	plt.legend()
	plt.axis('equal')

	plt.figure(2)
	mySystem.plotSim2DRelative(
	        [id(objects.state) for objects in CME if id(objects.state) != id(Earth.state)]
	        , id(Earth.state), labels)
	plt.legend()
	plt.axis('equal')

	fig = plt.figure(3)
	mySystem.plotSim3DRelative(
	        [id(objects.state) for objects in CME if id(objects.state) != id(Earth.state)]
	        , id(Earth.state), labels, fig = fig)
	plt.legend()
	plt.show()



if __name__ == '__main__':
	test()

#EOF
