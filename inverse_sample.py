# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:34:05 2021

@author: benmu


Sample the exponential distribution by using
The inverse CDF
"""
import matplotlib.pyplot as plt
import math
import numpy as np



# exponential distribution parameter
my_lambda = 3

# sample size
n = 1000000


# inverse exponential cdf
def inverse_cdf(x, my_lambda):
    return (math.log(1-x))/(-1*my_lambda)


# sample from uniform and evaluate w/ inverse
sample = np.random.rand(n)
inverse_sample = [inverse_cdf(x, my_lambda) for x in sample]

# plot inverted sample histogram
# alongside sample from true exponential
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].hist(inverse_sample)
ax[0].set_title("uniform sample inverse")
ax[1].hist(np.random.exponential(1/my_lambda, n), color='green')
ax[1].set_title(f'Sample from exponential, rate {my_lambda}')
plt.show()