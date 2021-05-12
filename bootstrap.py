# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:59:31 2021

@author: benmu

1. Draw a true mean from U(0,1)
    a. this will be the population mu for a normal distribution

2. take a small sample from a normal curve ~N(true_mu, 1)

3. Create 10000 boostrap samples n_runs times

4. Print how often the true mean falls outside of the middle 95% of
   Bootstrap sample means

Very dependent on the size and quality of our small sample!
"""

# Estimate true population mean by bootstrapping a small sample

import numpy as np

# how many times to create B boostrap samples
n_runs = 100

# sample size
n = 25

# Number of boostrapped samples per iteration
B = 1000

# confidence interval size
confidence = 0.95

# confidence interval percentiles
p_low = (1-confidence)/2
p_high = confidence + p_low

# track number of times true_mu not in CI
counter = 0

# create a true hidden mystery mean for our population
true_mu = np.random.rand()

# draw sample with size n from the population
small_sample = np.random.normal(loc=true_mu, size=n)

# preview the results by seeing how 'bad' the sample is
print(f'Population mean - sample mean: {np.mean(small_sample)-true_mu}')

# create B boostrap samples n_runs times
for i in range(n_runs):

    # track the resampled means
    means_list = []

    # create a resample and track its mean
    for boostrap in range(B):
        b_sample = np.random.choice(small_sample, size=n)
        means_list.append(np.mean(b_sample))

    # order bootstrap sample means
    means_list.sort()

    # add to counter if true_mu outside of middle 95% of resampled means
    if  (true_mu < means_list[int(B*p_low)]) or (true_mu > means_list[int(B*p_high)]):
        counter += 1


print(counter)
