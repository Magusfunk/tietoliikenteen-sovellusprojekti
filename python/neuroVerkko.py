import numpy as np
from icecream import ic

with open('test.npy', 'rb') as f:
    weights = np.load(f)
    biases = np.load(f)
    
ic(weights.shape, biases.shape)

for i in weights:
    for y in i:
        ic(y)