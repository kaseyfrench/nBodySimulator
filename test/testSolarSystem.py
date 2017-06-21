# solarSystem.py
#
# Kasey French, June 14th 2017
# ***********************************************************

from nbodysim import *
import matplotlib.pyplot as plt
import time
import numpy as np


def test():
	ssyvel = 2.00e4
	sszvel = 1.00e3
	Sun = MassParticle(1.989e30,
				 State(pos = [0.000e00, 0.000e04, 0.000e00],
				       vel = [0.000e00, ssyvel, sszvel + 0.000e00]))

	Mercury = MassParticle(3.3011e23,
	           State(pos = [4.566e10, 0.000e00, 5.606e09],
	                 vel = [0.000e00, ssyvel + 5.898e04, sszvel + 0.000e00]))

	Venus = MassParticle(4.868e24,
						State(pos = [1.082e11, 0.000e00, 0.000e00],
	             		vel = [0.000e00, ssyvel + 3.502e04, sszvel + 0.000e00]))

	Earth = MassParticle(5.972e24,
					 State(pos = [1.496e11, 0.000e00, 0.000e00],
	            	 vel = [0.000e00, ssyvel + 2.978e04, sszvel + 0.000e00]))

	Mars = MassParticle(6.417e23,
				 	State(pos = [2.280e11, 0.000e00, 0.000e00],
	             vel = [0.000e00, ssyvel + 2.407e04, sszvel + 0.000e00]))

	Jupiter = MassParticle(1.898e27,
						 State(pos = [7.787e11, 0.000e00, 0.000e00],
	                 vel = [0.000e00, ssyvel + 1.306e04, sszvel + 0.000e00]))

	Saturn = MassParticle(5.683e26,
	          State(pos = [1.434e12, 0.000e00, 0.000e00],
	                vel = [0.000e00, ssyvel + 9.680e03, sszvel + 0.000e00]))

	Uranus = MassParticle(8.681e25,
	         	State(pos = [2.872e12, 0.000e00, 0.000e00],
	         	      vel = [0.000e00, ssyvel+ 6.800e03, sszvel + 0.000e00]))

	Neptune = MassParticle(1.024e26,
	          	State(pos = [4.495e12, 0.000e00, 0.000e00],
	          	      vel = [0.000e00, ssyvel + 5.430e03, sszvel + 0.000e00]))

	Pluto = MassParticle(1.303e22,
	        	State(pos = [4.239e12, 0.000e00, 1.309e12],
	        	      vel = [0.000e00, ssyvel + 5.828e03, sszvel + 0.000e00]))

	newStar = MassParticle(2.400e32,
	          	State(pos = [1.000e13, 6.00e12, 0.000e00],
	                  vel = [-2.500e3, 0.000e00, sszvel + 0.000e00]))

	planetsAndSun = [Sun, Mercury, Venus, Earth, Mars, Jupiter,
									 Saturn, Uranus, Neptune, Pluto, newStar]

	myGrav = Gravity()

	mySystem = Nbodysim(planetsAndSun, [myGrav])

	tspan = np.linspace(0, 365 * 86400, 8000)
	mySystem.integrate(tspan)

	labels = {id(Sun.state) : "Sun" , id(Mercury.state) : "Mercury" ,
	 					id(Venus.state) : "Venus" , id(Earth.state) : "Earth" ,
	 					id(Mars.state) : "Mars" , id(Jupiter.state) : "Jupiter" ,
	 					id(Saturn.state) : "Saturn" , id(Uranus.state) : "Uranus" ,
	 					id(Neptune.state) : "Neptune" , id(Pluto.state) : "Pluto"}

	# fig = plt.figure(1)
	# plt.axis('equal')
	# system.plotSim2D(labels)
	# plt.legend()
	# # plt.savefig('samplesimulation.png', format = 'png', dpi = 500)

	# fig = plt.figure(2)
	# system.plotSim2DRelative([key for key in labels if key != id(Earth.state)],
	# 												  id(Earth.state), labels)
	# plt.legend()
	# # fig2 = plt.figure(2)
	# # system.plotSim3D(labels, fig = fig2)
	# # plt.legend()
	# plt.show()


	#mySystem.animate2D(xlim = [-1.1e13, 2.0e13], ylim = [-3.1e13, 3.0e13], labels = labels)
	#mySystem.animate3D(labels = labels)

if __name__ == '__main__':
	test()







#EOF