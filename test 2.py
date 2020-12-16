import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

def func(t, y, z):
    return y + z


t = np.linspace(0, 1.0, 100)
dt = t[1] - t[0]
z = np.random.rand(100)
output = np.empty_like(t)
r = ode(func).set_integrator("dop853")
r.set_initial_value(0, 0).set_f_params(z[0])

for i in range(len(t)):
    r.set_f_params(z[i])
    r.integrate(r.t + dt)
    output[i] = r.y

x = func(t, 15, z)
print(x)

plt.plot(t,x)
plt.show()