# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:49:13 2021

@author: Sabrina
"""

from numpy.random import random,choice
from numpy import cumsum, mean, array, polyfit, linspace, exp, sqrt
from numpy.linalg import norm
from pylab import plot, show
from scipy.optimize import curve_fit

class walk:
    def __init__(self):
        self.v = [0,0,0]
        
    def Step(self):
        self.v[0] = random()*choice([-1,1])
        self.v[1] = sqrt(1-self.v[0]**2)*random()*choice([-1,1])
        self.v[2] = sqrt(1-self.v[0]**2-self.v[1]**2)*choice([-1,1])
        return self.v
        
    def Walk(self,t):
        walk = array([0.0,0.0,0.0])
        for i in range(int(t)):
            walk += self.Step()
                
        magnitude2 = (walk[0]**2+walk[1]**2+walk[2]**2)
        return magnitude2
                
    def meanSquareDistance(self,t):
        walks = []
        for i in range(500):
            walks.append(self.Walk(t))
    
        return mean(walks)
    
    def Plot(self):
        t = linspace(1,100,100)
        y = [self.meanSquareDistance(t) for t in t]
        def curve(x,a1):
            return x*a1
        fit, err = curve_fit(curve, t, y, p0 = [1.0])
        plot(t,fit[0]*t, "r--")
        plot(t,y)
        show()
        print("Proportionality Constant:", fit[0])

lukeSkywalker = walk()
lukeSkywalker.Plot()
