# tesForce.py
#
# Kasey French, June 15th 2017
# ***************************************************************
# Note these are not real-life values for helium, simply a testing of what
# a neutral helium atom might look like.

from nbodysim import *
import numpy as np
import matplotlib.pyplot as plt

def test():

	# (2 protons and 2 neutrons in nucleus)
	protonNeutron = ChargedMass(1.836e03 * 4, 1.000e00,
	            	State(pos = [0.000e00, 0.000e00, 0.000e00],
	            	    	vel = [0.000e00, 0.000e00, 0.000e00]))

	# (2 electrons starting on opposite sides of nuclues)
	electron1 = ChargedMass(1.000e00, -1.000e00,
	              	State(pos = [3.100e01, 0.000e00, 0.000e00],
	              	      vel = [0.000e00, 1.4746e04, 0.000e00]))

	electron2 = ChargedMass(1.000e00, -1.000e00,
	              	State(pos = [-3.100e01, 0.000e00, 0.000e00],
	              	      vel = [0.000e00, -1.4746e04, 0.000e00]))

	system = Nbodysim([protonNeutron, electron1, electron2], Electromagnetism)
	tspan = np.linspace(0,.1,4000)

	""" Note that the integrator shows the electrons having weird trajectories for
	anything but small tspan. Might be becuase of simplicity of simulation, or
	becuase of an error, not sure)"""

	system.integrate(tspan)

	system.plotSim2D()

	plt.show()









if __name__ == '__main__':
	test()


#EOF