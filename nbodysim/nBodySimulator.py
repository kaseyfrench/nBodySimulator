# nBodySimulator.py
#
# Kasey French, May 28th 2017
# **********************************************************

from __future__ import print_function
from particle import *
from force import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy import vstack, array, squeeze, reshape, zeros, where
from collections import OrderedDict
from matplotlib import animation

class Nbodysim(object):

	def __init__(self, particleList, forceList):
		self.particleList = particleList
		self.forces = forceList
		self.particleStates = OrderedDict()
		self.tspan = None

		for p in self.particleList:
			self.particleStates[id(p.state)] = []

	def run(self, tspan):


		dt = tspan[1] - tspan[0] # Assumes evenly spaced out array for tspan
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


	def deriv(self, x, t):

		dx = zeros(x.shape)

		for i, p in enumerate(self.particleList):
			pj = [pj for pj in self.particleList if pj != p]
			p.state.pos = reshape(x[i*6:i*6+3], (3,1))
			p.state.vel = reshape(x[i*6+3:i*6+6], (3,1))

			for force in self.forces:

				dx[i*6+3:i*6+6] += reshape(force.computeAccel(p, pj), (3,))


		dx[0::6] = x[3::6]
		dx[1::6] = x[4::6]
		dx[2::6] = x[5::6]

		return dx

	def integrate(self, tspan):

		self.tspan = tspan
		# Upack initial state
		y0 = array([vstack([s.state.pos, s.state.vel]) for s in self.particleList])
		y0 = reshape(y0, (y0.size,))

		# Integrate
		y = odeint(self.deriv, y0, tspan)

		for i, s in enumerate(self.particleStates):
			self.particleStates[s] = y[:,i*6:i*6+3]

	def plotSim2D(self, labels = {}):

		for k,statelist in self.particleStates.iteritems():

			x = [state[0] for state in statelist]
			y = [state[1] for state in statelist]
			try:
				plt.plot(x, y, '.', label = labels[k])
			except:
				plt.plot(x, y, '.')



	def plotSim2DRelative(self, stateIDtarget, stateIDorigin,labels = {}):

		originStates = self.particleStates[stateIDorigin]
		for target in stateIDtarget:

			targetStates = self.particleStates[target]

			x = [t[0] - o[0] for t, o in zip(targetStates, originStates)]
			y = [t[1] - o[1] for t, o in zip(targetStates, originStates)]

			try:
				plt.plot(x, y, '.', label = labels[target])
			except:
				plt.plot(x, y, '.')

	def plotSim3D(self, labels = {}, fig = None):

		if fig is None:
			fig = plt.figure()

		ax = fig.add_subplot(111, projection = '3d')

		for k,statelist in self.particleStates.iteritems():

			x = np.squeeze(np.array([state[0] for state in statelist]))
			y = np.squeeze(np.array([state[1] for state in statelist]))
			z = np.squeeze(np.array([state[2] for state in statelist]))

			X, Y, Z = np.array(x), np.array(y), np.array(z)

			max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()

			Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
			Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
			Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())
			# Comment or uncomment following both lines to test the fake bounding box:
			for xb, yb, zb in zip(Xb, Yb, Zb):
				b = max([xb,yb,zb])
  			ax.plot([b], [b], [b], 'w')

			try:
				ax.plot(x, y, z, '.', label = labels[k])
			except:
				ax.plot(x, y, z, '.')


	def plotSim3DRelative(self, stateIDtarget, stateIDorigin, labels = {}, fig = None):

		if fig is None:
			fig = plt.figure()

		ax = fig.add_subplot(111, projection = '3d')

		originStates = self.particleStates[stateIDorigin]
		for target in stateIDtarget:


			targetStates = self.particleStates[target]

			x = [t[0] - o[0] for t, o in zip(targetStates, originStates)]
			y = [t[1] - o[1] for t, o in zip(targetStates, originStates)]
			z = [t[2] - o[2] for t, o in zip(targetStates, originStates)]
			X, Y, Z = np.array(x), np.array(y), np.array(z)

			max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()

			Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
			Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
			Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())
			# Comment or uncomment following both lines to test the fake bounding box:
			for xb, yb, zb in zip(Xb, Yb, Zb):
				b = max([xb,yb,zb])
  			ax.plot([b], [b], [b], 'w')

			try:
				ax.plot(x, y, z,'.',label = labels[target])
			except:
				ax.plot(x, y, z, '.')


	def animate2D(self, xlim, ylim, filename, nframes = None, labels = {}):

		if nframes is None:
			nframes = len(self.tspan)
		self.count = 0

		def plotFrame(n):

			print('Animating frame %d of %d' % (self.count, nframes), end = '\r')
			fig.clear()
			self.count += 1

			for k, statelist in self.particleStates.iteritems():

				x = statelist[n][0]
				y = statelist[n][1]
				try:
					plt.plot(x, y, '.', label = labels[k])
				except:
					plt.plot(x, y, '.')

				plt.axis('equal')
				ax = plt.gca()
				ax.set_ylim(ymin = ylim[0], ymax = ylim[1])
				ax.set_xlim(xmin = xlim[0], xmax = xlim[1])

			plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, 1.1),
	           ncol = 5, fancybox = True, shadow = True,
	           frameon = True, fontsize = 8)

		fig = plt.figure()
		n = len(self.tspan)
		frames = range(0, n, int(n / nframes))
		nframes = len(frames)

		anim = animation.FuncAnimation(fig, plotFrame, frames = frames, blit = False)

		Writer = animation.writers['ffmpeg']
		writer = Writer(fps = 60, bitrate = 1800)
		anim.save(filename + '.mp4', writer = writer)
		print('\n')


class Nbodyfixedcharges(Nbodysim):

	def __init__(self, particleList, forceList, fixedCharges):
		self.particleList = particleList
		self.forces = forceList
		self.particleStates = OrderedDict()
		self.fixedCharges = fixedCharges

		for p in self.particleList:
			self.particleStates[id(p.state)] = []

	def deriv(self, x, t):

		dx = zeros(x.shape)

		for fixed, rel in self.fixedCharges.iteritems():
			fixed.state.pos = rel['Particle'].state.pos + rel['State'].pos

		for i, p in enumerate(self.particleList):

			pj = [pj for pj in self.particleList if pj != p]
			p.state.pos = reshape(x[i*6:i*6+3], (3,1))
			p.state.vel = reshape(x[i*6+3:i*6+6], (3,1))

			pj.extend(self.fixedCharges.keys())

			for force in self.forces:
				dx[i*6+3:i*6+6] += reshape(force.computeAccel(p, pj), (3,))

		dx[0::6] = x[3::6]
		dx[1::6] = x[4::6]
		dx[2::6] = x[5::6]

		return dx











#EOF