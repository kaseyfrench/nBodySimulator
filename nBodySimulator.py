# nBodySimulator.py
#
# Kasey French, May 28th 2017
# **********************************************************

from particle import *
from force import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Nbodysim(object):

	def __init__(self, particleList, force):
		self.particleList = particleList
		self.force = force()
		self.particleStates = {}

		for p in self.particleList:
			self.particleStates[id(p.state)] = []

	def run(self, tspan):

		
		dt = tspan[1]-tspan[0] # Assumes evenly spaced out array for tspan
		for k in tspan:
			
			tempparticleList = np.copy(self.particleList)

			for pi in self.particleList:
				# print 'pos: ', pi.state.pos
				# print 'mass: ', pi.mass
				# input('')

				pjList = [pj for pj in tempparticleList if pj != pi]
				a = self.force.computeAccel(pi,pjList)					
				pi.state.pos += pi.state.vel*dt+.5*a*dt**2
				pi.state.vel += a*dt
				# print len(pjList)
				self.particleStates[id(pi.state)].append(np.copy(pi.state.pos))

		return self.particleStates

	def plotSim2D(self):

		plt.figure()	
		plt.axis('equal')

		for k,statelist in self.particleStates.iteritems():

			x = [state[0] for state in statelist]
			y = [state[1] for state in statelist]

			plt.plot(x,y,'.')	

	def plotSim3D(self):

		fig = plt.figure()

		ax = fig.add_subplot(111, projection = '3d')

		for k,statelist in self.particleStates.iteritems():

			x = np.squeeze(np.array([state[0] for state in statelist]))
			y = np.squeeze(np.array([state[1] for state in statelist]))
			z = np.squeeze(np.array([state[2] for state in statelist]))

			ax.plot(x,y,z)

			








#EOF