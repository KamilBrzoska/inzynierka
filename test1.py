import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def equations1(Xbh, t):
    Ss = 1
    So = 2
    Sno = 1
    Uh = 2
    Ks = 20
    Koh = 0.2
    Ng = 0.8
    Kno = 0.5

    if t > 3.0:
        Bh = 1
    else:
        Bh = 2

    DXbhDT = ((Uh * Ss) / (Ks + Ss)) * ((Xbh * So) / (Koh + So)) + Ng * Uh * (Ss / (Ks + Ss)) * (Koh / (Koh + So)) * (
            Sno / (Kno + Sno)) * Xbh - Bh * Xbh
    return (DXbhDT)


# print (equations(1))

x0 = [1000]
t = np.linspace(0, 15, 1000)
Xbh = odeint(equations1, x0, t)



plt.plot(t,Xbh)
plt.show()

def equations2 (Xba,t):
    Ua = 1
    Snh = 1
    Knh = 0.01
    So = 2
    Koa = 0.4
    Ba = 0.15

    DXbaDT = Ua*(Snh/(Knh+Snh))*(So/(Koa+So))*Xba-Ba*Xba
    return (DXbaDT)
x1 = [15, 0.5, 7]
t1 = np.linspace(0, 7, 1000)
Xba = odeint(equations2, x1, t1)



plt.plot(t1,Xba)
plt.show()