# particle.py
#
# Kasey French, May 27th 2017
# *****************************************************************************

from numpy import zeros, array, reshape, random

class State(object):

	def __init__(self, pos =  zeros((3,1)), vel =  zeros((3,1)), acc = zeros((3,1))):

		self.pos = reshape(array(pos), (3,1))
		self.vel = reshape(array(vel), (3,1))
		self.acc = reshape(array(acc), (3,1))

	def display(self):
		print '\nID: ',id(self)
		print 'Position: \n', self.pos
		print 'Velocity: \n', self.vel
		print 'Acceration: \n', self.acc

class Particle(object):

	def __init__(self, state = State()):

		self.state = state
		self.type = 'Particle'

	def getType(self):
		return self.type

class MassParticle(Particle):

	def __init__(self, mass, state = State()):
		super(MassParticle, self).__init__(state)

		if mass <= 0:
			raise ValueError('Error in MassParticle(): mass must be positive!')

		self.mass = mass
		self.type = 'Mass'

class ChargedParticle(Particle):

	def __init__(self, charge, state = State()):
		super(ChargedParticle, self).__init__(state)

		self.charge = charge
		self.type = 'Charge'

class electron(MassParticle, ChargedParticle):

	# Units are in atomic scales
	def __init__(self, state = State()):
		# super(electron, self).__init__(state) <--- why doesn't this work?

		self.charge = -1.0
		self.mass = 1.0
		self.type = 'electron'
		self.state = state

class proton(MassParticle, ChargedParticle):

	# Units are in atomic scales
	def __init__(self, state = State()):
		# super(proton, self).__init__(state) <--- why doesn't this work?

		self.charge = 1.0
		self.mass = 1836.0
		self.type = 'proton'
		self.state = state

class neutron(MassParticle, ChargedParticle):

	# Units are in atomic scales
	def __init__(self, state = State()):
		# super(neutron, self).__init__(state) <--- why doesn't this work?

		self.charge = 0
		self.mass = 1836.0
		self.type = 'neutron'
		self.state = state

class ChargedMass(MassParticle, ChargedParticle):

	def __init__(self, mass, charge = 0, state = State()):
		# super(ChargedMass, self).__init__(state) <--- why doesn't this work?

		self.charge = charge
		self.mass = mass
		self.type = 'charged mass'
		self.state = state

class ChargedMassFactory(object):

	def __init__(self):
		pass

	def generateRandomChargedMasses(self, n, meanpos, stdpos,
	                                meanvel, stdvel, meanmass,
	                                stdmass, meancharge, stdcharge):

		particleList = []
		meanpos = reshape(array(meanpos),(3,1))
		meanvel = reshape(array(meanvel),(3,1))
		for i in range(n):
			s = State(pos = meanpos+stdpos*random.standard_normal((3,1)),
			          vel = meanvel+stdvel*random.standard_normal((3,1)))
			m = meanmass+random.standard_normal((1,1))*stdmass
			c = meancharge+random.standard_normal((1,1))*stdcharge
			particleList.append(ChargedMass(m, c, s))

		return particleList

class MassFactory(object):

	def __init__(self):
		pass

	def generateRandomMasses(self, n, meanpos, stdpos,
	                         meanvel, stdvel, meanmass,
	                         stdmass):

		particleList = []

		for i in range(n):
			s = State(pos = meanpos+stdpos*random.standard_normal((3,1)),
			          vel = meanvel+stdvel*random.standard_normal((3,1)))
			m = meanmass+random.standard_normal((1,1))*stdmass
			particleList.append(MassParticle(m,s))

		return particleList










#EOF