import matplotlib.pyplot as plt
import numpy as np

def fplots(wl, tc, leg = '', col = ''):
    """Plots the transmission curve of a filter"""
    plt.plot(wl, tc/max(tc), label=leg, color=col)
    plt.xscale('log', basex=10)
    plt.ylim(0, 1)
    plt.xlim(1000, 25000)
    plt.yticks(np.arange(0, 1.1, step=0.2), [0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    plt.xticks([1000, 1400, 1700, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000,
                13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000], [])
    plt.tick_params(axis='x', which='both', bottom=True, top=True, direction='in')
    plt.tick_params(axis='y', which='both', left=True, right=True, direction='in')
    plt.grid(True)






