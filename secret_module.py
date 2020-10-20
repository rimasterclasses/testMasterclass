import matplotlib.pyplot as plt
import numpy as np
# if using a Jupyter notebook, includue:
#%matplotlib inline

def do_a_maths(mu, sigma):
    mu = 80
    sigma = 7
    x = np.random.normal(mu, sigma, size=1000)

    plt.hist(x, 20,
             density=True,
             histtype='bar',
             facecolor='b',
             alpha=0.5)

    plt.show()