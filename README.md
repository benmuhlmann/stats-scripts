# stats-scripts
sampling methods and more
1. Bootstrap CI example
  - randomly chooses a true_mu for a normal distribution with mean=true_mu, sigma=1
  - samples from above Normal distribution
  - gets B boostrap samples of the above sample several times
  - outputs how often true_mu falls outside specified 'confidence' interval (middle range (e.g. 95%) of B boostrap means)

2. Inverse sampling 
  - Draws n samples from the exponential CDF's inverse
  - plots a histogram of the n samples alongside a histogram of n draws from the original exponential
	- to prove they're the same

3. Rejection sampling
  - take n (x,y) pairs from X in (-4,4) (where most of the standard normal falls between) and Y in (0,1) (inefficient rejection sampling given the true height of the standard normal, I know)
  - accept pair if y < f(x), where f is the standard normal pdf
  - plot accepted and rejected pairs separately 