# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:30:45 2021

@author: benmu

Simulate the normal distribution.

Take n coordinate pairs where 
X in (-4,4)
Y in (0,1)

keep points if y < f(x), where f is the std normal distribution
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# number of data pairs to plot for rejection/acceptance
n = 10000

# target density
def normal_pdf(x):
    return ((2*math.pi)**-0.5)*math.exp((-(1*x)**2)/2)

# sample n x values and y values
x = np.random.uniform(low=-4, high=4, size=n)
y = np.random.uniform(low=0, high=1, size=n)
keep_x = []
keep_y = []

reject_x = []
reject_y = []

# keep x and y pairs if y < f(x)
for i in range(n):
    if y[i] < normal_pdf(x[i]):
        keep_x.append(x[i])
        keep_y.append(y[i])
    else:
        reject_x.append(x[i])
        reject_y.append(y[i])

# plot accepted x,y pairs.     
fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].scatter(keep_x, keep_y)
ax[0].set_ylim(0,1)
ax[0].set_xlim(-4.1,4.1)
ax[0].set_title('Accepted data points')

# plot rejected x,y pairs
ax[1].scatter(reject_x, reject_y, color='green')
ax[1].set_ylim(0,1)
ax[1].set_xlim(-4.1,4.1)
ax[1].set_title('Rejected data points')
plt.show()
