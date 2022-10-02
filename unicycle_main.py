import numpy as np 
from unicycle import Unicycle
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

metadata = dict(title = 'Movie Test', artist = "Matplotlib", comment = "Movie support!")
writer = FFMpegWriter(fps=15, metadata = metadata)


plt.ion()
fig = plt.figure()
ax = plt.axes(xlim = (0,7), ylim = (-0.5,8))

robot = Unicycle(np.array([0,0,0]).reshape(-1,1), 0.01, ax)

with writer.saving(fig, 'test.mp4', 100):

	for i in range(1000):
		v = 1.0
		w = np.pi/6
		u = np.array([v,w]).reshape(-1,1)
		robot.step(u)
		robot.render_plot()
		
		fig.canvas.draw()
		fig.canvas.flush_events()
	
		writer.grab_frame()



plt.ioff() 
print("DONE!")