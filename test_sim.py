import numpy as np
import matplotlib.pyplot as plt

print("hi")

T = 10
dt = 0.1
N = int(T/dt)

X0 = np.array([0])
X = np.copy(X0)

for t in range( N ):
	print('start for loop ')
	ut = 0.5
	X_next = X + ut * dt
	X = np.append( X, X_next )

plt.figure()
plt.plot( X )
plt.show()