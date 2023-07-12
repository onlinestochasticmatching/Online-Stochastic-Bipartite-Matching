import math
import numpy as np


def g(x,theta):
	return (1 - (1-theta)*(x/(1-theta) - math.floor(x/(1-theta))) ) * (theta ** math.floor(x/(1-theta)))

def bound(x,epsilon,delta,theta):
	return 1- g(x*(1-epsilon),theta)*math.exp(-(1+delta)*(1-x))

N = 1000000
epsilon = 0.11
delta = 0.18
theta_hat = (1-epsilon) * delta/(delta + epsilon)
print(min([bound(x,epsilon, delta,theta_hat) for x in np.linspace(0,1,N)]))