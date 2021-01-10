import pandas as pd
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import matplotlib.ticker as mticker

f = Figure(figsize=(5, 5), dpi=100)
ax = f.add_subplot(111, projection='3d')


def _refit_artists():
    ax.relim()
    ax.autoscale_view()
    ax.set_autoscale_on(True)

def graphs_settler(i):

    data = pd.read_csv('data.csv')


    z = np.array([data['layer1'], data['layer2'], data['layer3'], data['layer4'], data['layer5'], data['layer6'],
                  data['layer7'], data['layer8'], data['layer9'], data['layer10']])
    x = data['t']
    y = np.array([data['1'], data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'],
                  data['9'], data['10']])

    ax.clear()

    plt.gca().xaxis.set_major_locator(mticker.MaxNLocator())
    plt.tight_layout()
    ax.mouse_init()
    _refit_artists()


