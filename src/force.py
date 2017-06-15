# force.py
#
# Kasey French, May 27th 2017
# *****************************************************************

import numpy as np
from particle import *
from abc import ABCMeta, abstractmethod

class Force(object):


	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	@abstractmethod
	def computeAccel(self, effected, effectors):		
		pass
 



class Gravity(Force):
	def computeAccel(self, effected, effectors):

		acc = np.zeros((3,1))
		for effector in effectors:

			r = effector.state.pos-effected.state.pos
			r3 = np.linalg.norm(r)**3
			
			acc += (6.67408e-11 * effector.mass)/r3 * r

		return acc

class Electromagnetism(Force):

	def computeAccel(self,effected, effectors):

		acc = np.zeros((3,1))
		for effector in effectors:

			r = effector.state.pos-effected.state.pos
			r3 = np.linalg.norm(r)**3

			acc += (8.98755e9 * effector.charge)/r3 * r /(effected.mass)


		return acc	









#EOF