import math
import numpy as np

def g(x,theta):
	return (1 - (1-theta)*(x/(1-theta) - math.floor(x/(1-theta))) ) * (theta ** math.floor(x/(1-theta)))

def apxAtT(theta, x, y):
	if y == 0:
		return 1 - g(x,theta)*math.exp(-1*(1-x))
	return 1-g(x, theta) *  ((1 - y/(1-x)) ** ( (1-x)*(1-x)/y))

# computes the smallest value of apxAtT(theta, x, y) - a - b*x - c*y on a grid with spacing 1/N
def smallestGap(a,b,c,N):
	currentMin = 1
	for x in np.linspace(0,1,N):
		for y in np.linspace(0,1,N):
			if y <= (1-x) ** 2:
				gap = apxAtT(theta,x,y) - a - b*x - c*y
				if gap < currentMin:
					currentMin = gap
	return currentMin

a = 0.614
b = 0.122
c = 0.197
theta = 0.5
print(smallestGap(a,b,c,10000))