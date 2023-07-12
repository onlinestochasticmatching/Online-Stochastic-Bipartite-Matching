import math
import numpy as np

def g(x,theta):
	return (1 - (1-theta)*(x/(1-theta) - math.floor(x/(1-theta))) ) * (theta ** math.floor(x/(1-theta)))

def bound(x,epsilon,delta,theta):
	return 1- g(x*(1-epsilon),theta)*math.exp(-(1+delta)*(1-x))

N = 10000

bestEps = -1
bestDelta = -1
bestBound = 0
for epsilon in np.linspace(0.01, 1, 100):
	for delta in np.linspace(0.01, 1, 100):
		theta_hat = (1-epsilon) * delta/(delta + epsilon)
		M = min([bound(x, epsilon, delta, theta_hat) for x in np.linspace(0,1,N)])
		if M > bestBound:
			bestBound = M
			bestEps = epsilon
			bestDelta = delta

print(bestBound, bestEps, bestDelta)
