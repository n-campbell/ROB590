import numpy as np
import cvxpy as cv

class Unicycle:
	def __init__(self, x0, dt, ax):
		self.X = x0
		self.dt = dt
		
		self.body = ax.scatter([],[],[])
		self.render_plot()

	def render_plot(self):
		v = 1.0
		w = np.pi/6
		u = np.array([v,w]).reshape(-1,1)
		self.step(u)
		self.body._offsets3d = (self.X[0, 0,0], self.X[1, 0, 0], self.X[1, 0, 0])
		
	def f(self):
		return np.array([0,0,0]).reshape(-1,1)

	def g(self):
		return np.array([ [np.cos(self.X[2,0,0]), 0], 
						  [np.sin(self.X[2,0,0]), 0],
						   [0, 1]  ])

	def step(self, U):
		self.X = self.X + (self.f() + self.g() @ U) * self.dt


