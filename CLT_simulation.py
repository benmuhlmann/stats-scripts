# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:05:52 2021

@author: benmu
"""
import numpy as np
import matplotlib.pyplot as plt
plt.figure()
plt.hist(np.random.exponential(1,1000000), bins=20)
plt.show()

n_list = [2, 20, 50, 100]
num_samples = 100000

fig, ax = plt.subplots(1, len(n_list), figsize=(24, 5))

for i, n in enumerate(n_list):
    samples = [np.random.exponential(1, n) for sample in range(num_samples)]
    means = [np.mean(sample) for sample in samples]
    ax[i].hist(means, bins=20)
    ax[i].set_title(f'n = {n}')
    
plt.show()
