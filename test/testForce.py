# tesForce.py
#
# Kasey French, May 27th 2017
# ***************************************************************
# Directories need to be clarified-create particle,force modules.
from force import *
from particle import *

def test():

	m1 = MassParticle(60., State(pos = [6.378e6,0.,0.]))
	m2 = MassParticle(5.972e24)

	m3 = MassParticle(1.898e27, State(pos = [3.84e8,0.,0.]))

	grav = Gravity()

	accMass = grav.computeAccel(m1,[m2,m3])

	electroncharge = -1.602e-19
	protoncharge = 1.602e-19

	c1 = ChargedParticle(electroncharge, State(pos = [5.e-6,0.,0.]))
	c2 = ChargedParticle(protoncharge, State(pos = [0.,0.,0.]))

	electro = Electromagnetism()

	accElectro = electro.computeAccel(c1,[c2]) 

	print accMass
	print accElectro






if __name__ == "__main__":
	test()




#EOF