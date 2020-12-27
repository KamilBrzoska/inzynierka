import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

Xbh = 0.1
Xba = 0.1
Ss = 0.32
Xs = 0.1
Xp = 0.2
Xnd = 0.001
Snd = 0.002
Snh = 0.9
Sno = 0.02
So = 0.5

        #
Uh = 6.98  #
Ks = 0.3  #
Koh = 0.156  #
Ng = 0.5  #
Kno = 0.1  #
Bh = 0.62  #
Ua = 0.0676  #
Knh = 0.109  #
Koa = 0.25  #
Ba = 0.0289  #
Kh = 12.7  #
Yh = 0.666  #
Kx = 0.302  #.
Nh = 0.192  #
Fp = 0.08  #
Ixb = 0.068  #
Ka = 25  #
Ya = 0.206  #
Ixp = 0.068  #
        # t = [0.0, 0.1]
t = np.linspace(0,100)
# t = [0.1,0.2]

def equationss(solution, t):
    Xbh=solution[0]
    Xba=solution[1]
    Ss=solution[2]
    Xs=solution[3]
    Xp=solution[4]
    Xnd=solution[5]
    Snd=solution[6]
    Snh=solution[7]
    Sno=solution[8]
    So=solution[9]
    dXbhdt = ((Uh * Ss) / (Ks + Ss)) * (
            (Xbh * So) / (Koh + So)) + Ng * Uh * (
                     Ss / (Ks + Ss)) * (
                     Koh / (Koh + So)) * (
                     Sno / (Kno + Sno)) * Xbh - Bh * Xbh

    dXbadt = Ua * (Snh / (Knh + Snh)) * (
            So / (Koa + So)) * Xba - Ba * Xba

    dSsdt = ((-Uh / Yh) * (Ss / (Ks + Ss)) * (
            (So / (Koh + So)) + Ng * (Koh / (Koh + So)) * (
            Sno / (Kno + Sno))) + Kh * (
                     (Xs / Xbh) / (Kx + (Xs / Xbh))) * (
                     (So / (Koh + So)) + Nh * (Koh / (Koh + So)) * (
                     Sno / (Kno + Sno)))) * Xbh

    dXsdt = (1 - Fp) * (Bh * Xbh + Ba * Xba) - Kh * (
            (Xs / Xbh) / (Kx + (Xs / Xbh))) * (
                    (So / (Koh + So)) + Nh * (Koh / (Koh + So)) * (
                    Sno / (Kno + Sno))) * Xbh

    dXpdt = Fp * (Bh * Xbh + Ba * Xba)

    dXnddt = (Ixb - Fp * Ixp) * (Bh * Xbh + Ba * Xba) - Kh * (
            (Xnd / Xbh) / (Kx + (Xs / Bh))) * (
                     (So / (Koh + So)) + Nh * (Koh / (Koh + So)) * (
                     Sno / (Kno + Sno))) * Xbh

    dSnddt = (-Ka * Snd + Kh * ((Xnd / Xbh) / (Kx + (Xs / Bh))) * (
            (So / (Koh + So)) + Nh * (Koh / (Koh + So)) * (
            Sno / (Kno + Sno)))) * Xbh

    dSnhdt = (-Ixb * Uh * (Ss / (Ks + Ss)) * (
            (So / (Koh + So)) + Ng * (Koh / (Koh + So)) * (
            Sno / (Kno + Sno))) + Ka * Snd) * Xbh - Ua * (
                     Ixb + 1 / Ya) * (Snh / (Knh + Snh)) * (
                     So / (Koa + So)) * Xba

    dSnodt = -Uh * Ng * ((1 - Yh) / (2.86 * Yh)) * (Ss / (Ks + Ss)) * (
            Koh / (Koh + So)) * (
                     Sno / (Kno + Sno)) * Xbh + (
                     Ua / Ya) * (Snh / (Knh + Snh)) * (
                     So / (Koa + So)) * Xba

    dSodt = -Uh * ((1 - Yh) / Yh) * (Ss / (Ks + Ss)) * (
            So / (Koh + So)) * Xbh - Ua * ((4.57 - Ya) / Ya) * (
                    Snh / (Knh + Snh)) * (So / (Koa + So)) * Xba

    return [dXbhdt, dXbadt, dSsdt, dXsdt, dXpdt, dXnddt, dSnddt, dSnhdt, dSnodt, dSodt]

Uzero = [Xbh,Xba,Ss,Xs,Xp,Xnd,Snd,Snh,Sno,So]

solution = odeint(equationss, Uzero, t)

print (solution)
plt.plot(t, solution[:, 0])
plt.plot(t, solution[:, 1])
plt.plot(t, solution[:, 2])
plt.plot(t, solution[:, 3])
plt.plot(t, solution[:, 4])
plt.plot(t, solution[:, 5])
plt.plot(t, solution[:, 6])
plt.plot(t, solution[:, 7])
plt.plot(t, solution[:, 8])
plt.plot(t, solution[:, 9])
plt.show()