# tesForce.py
#
# Kasey French, June 15th 2017
# ***************************************************************

from src.force import *
from src.particle import *

def test():

	e = electron(State(pos = [1,20,0]))
	p = proton(State(vel = [4,3,2]))
	n = neutron(State(pos = [0, 6, 0]))
	star = ChargedMass(100, 70, State(pos = [3, 2, 1]))
	print e.type
	print p.charge
	print p.mass
	e.state.display()    # Note print e.state does not work #
	p.state.display()
	n.state.display()
	star.state.display()
	print star.type
	print star.charge
	print star.mass

if __name__ == '__main__':
	test()

#EOF