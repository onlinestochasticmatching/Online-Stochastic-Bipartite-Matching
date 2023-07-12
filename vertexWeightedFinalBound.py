import math
import numpy as np

def g(x, theta):
	return (1 - (1-theta)*(x/(1-theta) - math.floor(x/(1-theta))) ) * (theta ** math.floor(x/(1-theta)))

def varBound(S_L, S_H):
	return 1 - 0.5 * math.sqrt( S_L + S_H - S_L * (1 - theta + S_L / 2) - S_H*S_H/2)

def fracBound(theta, S_H, a, b, c):
	return a + b*theta + c*S_H*S_H/2

def apxRatio(a, b, c, N):
	currentMin = 1
	for S_L in np.linspace(0, theta, N):
		for S_H in np.linspace(0.25, 1-theta, N):
			M = max(varBound(S_L,S_H), fracBound(theta, S_H, a, b, c))
			if M < currentMin:
				currentMin = M
	return currentMin

a = 0.614
b = 0.122
c = 0.197
theta = 0.5
print(apxRatio(a, b, c, 10000))
