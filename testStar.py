# tesForce.py
#
# Kasey French, June 15th 2017
# ***************************************************************

from src.force import *
from src.particle import *
from src.nBodySimulator import *
import numpy as np
import matplotlib.pyplot as plt

def test():
	
	protonNeutron = ChargedMass(1.836e03 * 4, 1.000e00, 
	            	State(pos = [0.000e00, 0.000e00, 0.000e00], 
	            	    	vel = [0.000e00, 0.000e00, 0.000e00]))

	electron1 = ChargedMass(1.000e00, -1.000e00, 
	              	State(pos = [3.100e01, 0.000e00, 0.000e00], 
	              	      vel = [0.000e00, 1.4746e04, 0.000e00]))

	electron2 = ChargedMass(1.000e00, -1.000e00, 
	              	State(pos = [-3.100e01, 0.000e00, 0.000e00], 
	              	      vel = [0.000e00, -1.4746e04, 0.000e00]))

	system = Nbodysim([protonNeutron, electron1, electron2], Electromagnetism)
	tspan = np.linspace(0,.1,4000)
	system.integrate(tspan)

	system.plotSim2D()

	plt.show()









if __name__ == '__main__':
	test()


#EOF