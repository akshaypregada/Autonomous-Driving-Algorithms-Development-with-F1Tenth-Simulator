# bayesian_estimation.py

import numpy as np

def bayesian_update(prior, likelihood):
    """
    Performs a Bayesian update given a prior and likelihood.
    """
    posterior = prior * likelihood
    posterior /= np.sum(posterior)
    return posterior

if __name__ == "__main__":
    prior = np.array([0.2, 0.3, 0.5])
    likelihood = np.array([0.8, 0.6, 0.4])
    posterior = bayesian_update(prior, likelihood)
    print("Updated Posterior:", posterior)
