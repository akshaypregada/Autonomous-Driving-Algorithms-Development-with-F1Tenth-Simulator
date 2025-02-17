# bayesian_filter.py

import numpy as np

def bayesian_update(prior, likelihood):
    """
    Perform Bayesian filter update.
    """
    posterior = prior * likelihood
    posterior /= np.sum(posterior)
    return posterior

if __name__ == "__main__":
    prior = np.array([0.2, 0.5, 0.3])
    likelihood = np.array([0.8, 0.6, 0.4])
    updated_posterior = bayesian_update(prior, likelihood)
    print("Updated Posterior:", updated_posterior)
