#!/usr/bin/env python3

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

def brown(T, N, N_ens=1):
    dt = T / N
    sqrt_dt = np.sqrt(dt)

    dW = random.normal(0., sqrt_dt, (N_ens, N))
    W = np.zeros((N_ens, N + 1))
    W[:, 1:] = np.cumsum(dW, axis=1)

    return W, dW

if __name__ == "__main__":
    random.seed(0)

    T = 1.
    N = 500
    t = np.linspace(0., 1., N+1)

    N_ens = 100
    W_ens, dW_ens = brown(T, N, N_ens)

    for k in range(N_ens):
        plt.plot(t, W_ens[k, :])

    print(np.sum(W_ens[:, -1]**2) / N_ens)
    plt.show()
