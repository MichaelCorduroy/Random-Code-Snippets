import numpy as np 
import random 

# import training data
data = songdata.r 

# sigmoid activation function
def sigmoid(z):
    return 1/ (1 + np.exp(-z))

# Random Initialization of Weights
w1 = []
for i in range(12):
    v = random.random() * 0.1
    w1.append(v)

w2 = []
for ii in range(8):
    v = random.random() * 0.1
    w2.append(v)

# training iteration
for n in range(100):
    for k in range(data):
        # init input nodes
        a = data[k][0]
        b = data[k][1]
        c = data[k][3]

        
