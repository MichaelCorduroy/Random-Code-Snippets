#This is my perceptitron

import numpy as np 

def sigmoid(x, deriv=False):
    if deriv == True:
        return x * (1-x)
    return 1/(1 + np.exp(-x))

x = np.array([[0,1,0],[1,0,0],[0,0,1],[1,1,1]])
y = np.array([[0,0,1,1]]).T

np.random.seed(1)

syn0 = 2 * np.random.random((3,1)) - 1

for _ in range(10000):
    l0 = x
    l1 = sigmoid(np.dot(l0, syn0))
    l1_error = y - l1
    l1_delta = l1_error * sigmoid(l1, True)

    syn0 += np.dot(l0.T, l1_delta)
print(l1)

while(True):
    tree = []
    for _ in range(3):
        w = int(input("Whats the number?"))
        tree.append(w)

    v = np.array([tree])
    v1 = sigmoid(np.dot(v, syn0))
    print(v1)
    
    print(tree)

    e  = float(input("What was the right answer?"))


    l1_error = e - l1
    l1_delta = l1_error * sigmoid(l1, True)

    np.append(x,v)
    l0 = x
    syn0 += np.dot(l0.T, l1_delta)

