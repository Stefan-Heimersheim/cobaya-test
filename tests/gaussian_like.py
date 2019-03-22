from scipy.stats import multivariate_normal
from time import sleep
import numpy as np

mean = [0, 0, 0, 0, 0]
cov = [[1,0,0,0,0],[0,0.5,0,0,0],[0,0,0.25,0,0],[0,0,0,0.1,0],[0,0,0,0,0.05]]

last_values = np.array([0,0,0,0,0])

def loglike(a,b,c,d,e):
    values = np.array([a,b,c,d,e])
    global last_values
    changed = np.array(["a","b","c","d","e"])[np.where(values != last_values)]
    last_values = values
    print("changed: %r"%list(changed))
    sleep(1)
    return multivariate_normal.logpdf(values, mean=mean, cov=cov)
    
    
