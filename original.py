import numpy as np
import random


dataa = [[3, 4, 0], [20,17,1], [2, 5, 0], [21, 19,]]

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Random Initialization of weights
w1 = []
for i in range(len(w1)):
    v = random.random() * 0.1
    w1.append(v)

w2 = []
for ii in range(len(w2)):
    v = random.random() * 0.1
    w2.append(v)

w3 = []
for iii in range(len(w3)):
    v = random.random() * 0.1
    w3.append(v)

# init input layer
na1 = dataa[0]
na2 = dataa[1]

# train
for i in range(0,100):
    for u in range(len(dataa)):
        na1 = dataa[u][0]
        na2 = dataa[u][1]
        # init first node
        nb1 = sigmoid( (na1 * w1[0]) + (na2 * w1[2]) + 1 )

        # init second node
        nb2 = sigmoid( (na1 * w1[1]) + (na2 * w1[3]) + 1 )

        # init output one
        nc1 = sigmoid( (nb1 * w2[0]) + (nb2 * w2[2]) + 1 )

        # init output two
        nc2 = sigmoid( (nb1 * w2[1]) + (nb2 * w2[3]) + 1 )

        # init conclusion
        vvs = sigmoid( (nc1 * w3[0]) + (nc2 * w3[1]) + 1 )

        '''
        print('--Output 1:')
        print(nc1)
        print('--Output 2:')
        print(nc2)
        print('--Conclusion')
        print(vvs)
        '''
        # calculate error
        error = dataa[2] - vvs
        # adjust weights
        delta = error * (vvs * (1 - vvs))
        for d in range(len(w1)):
            w1[d] += delta
        for dd in range(len(w2)):
            w2[dd] += delta
        for ddd in range(len(w3)):
            w3[ddd] += delta

print(vvs)

while(True):
    haa = []
    for b in range(2):
        yy = int(input("number? "))
        haa.append(yy)
    na1 = yy[0]
    na2 = yy[1]
    # init first node
    nb1 = sigmoid( (na1 * w1[0]) + (na2 * w1[2]) + 1 )

    # init second node
    nb2 = sigmoid( (na1 * w1[1]) + (na2 * w1[3]) + 1 )

    # init output one
    nc1 = sigmoid( (nb1 * w2[0]) + (nb2 * w2[2]) + 1 )

    # init output two
    nc2 = sigmoid( (nb1 * w2[1]) + (nb2 * w2[3]) + 1 )

    # init conclusion
    vvs = sigmoid( (nc1 * w3[0]) + (nc2 * w3[1]) + 1 )

    print(vvs)

    # calculate error
    error = dataa[2] - vvs
    # adjust weights
    delta = error * (vvs * (1 - vvs))
    for d in range(len(w1)):
        w1[d] += delta
    for dd in range(len(w2)):
        w2[dd] += delta
    for ddd in range(len(w3)):
        w3[ddd] += delta

