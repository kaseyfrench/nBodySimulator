# testParticle.py
#
#Kasey French May 27th 2017
# ******************************************************************

from particle import *

def test():

	state1 = State()
	state1.display()

	state2 = State(pos = [1,2,3], vel = [.5,3./2,7.2],acc = [1,1,1])
	state2.display()

	p1 = Particle()
	p1.state.display()

	p2 = Particle(state1)
	p2.state.display()

	m1 = MassParticle(10)
	m1.state.display()

	c1 = ChargedParticle(-1)
	c1.state.display()


if __name__ == "__main__":
	test()













#EOF