from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from test import reactor_ASM1


model = reactor_ASM1()
x = reactor_ASM1.graphs

ani = FuncAnimation(plt.gcf(), x, interval=1000)

plt.tight_layout()
plt.show()


