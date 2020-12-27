import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
from itertools import count
import pandas as pd
import matplotlib.ticker as mticker


class reactor_ASM1:

    def __init__(self):
        self.Xbh = 0.1
        self.Xba = 0.1
        self.Ss = 0.32
        self.Xs = 0.1
        self.Xp = 0.2
        self.Xnd = 0.001
        self.Snd = 0.002
        self.Snh = 0.9
        self.Sno = 0.02
        self.So = 0.5

        #
        self.Uh = 6.98  #
        self.Ks = 0.3  #
        self.Koh = 0.156  #
        self.Ng = 0.5  #
        self.Kno = 0.1  #
        self.Bh = 0.62  #
        self.Ua = 0.0676  #
        self.Knh = 0.109  #
        self.Koa = 0.25  #
        self.Ba = 0.0289  #
        self.Kh = 12.7  #
        self.Yh = 0.666  #
        self.Kx = 0.302  #
        self.Nh = 0.192  #
        self.Fp = 0.08  #
        self.Ixb = 0.068  #
        self.Ka = 25  #
        self.Ya = 0.206  #
        self.Ixp = 0.068  #
        self.t = [0.0, 0.1]
        # self.t = np.linspace(0, 100, 30)

    def equationss(self, U, t):
        self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So = U
        DXbhDT = ((self.Uh * self.Ss) / (self.Ks + self.Ss)) * (
                (self.Xbh * self.So) / (self.Koh + self.So)) + self.Ng * self.Uh * (
                         self.Ss / (self.Ks + self.Ss)) * (
                         self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno)) * self.Xbh - self.Bh * self.Xbh

        DXbaDT = self.Ua * (self.Snh / (self.Knh + self.Snh)) * (
                self.So / (self.Koa + self.So)) * self.Xba - self.Ba * self.Xba

        DSsDT = ((-self.Uh / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno))) + self.Kh * (
                         (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno)))) * self.Xbh

        DXsDT = (1 - self.Fp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                        (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                        self.Sno / (self.Kno + self.Sno))) * self.Xbh

        DXpDT = self.Fp * (self.Bh * self.Xbh + self.Ba * self.Xba)

        DXndDT = (self.Ixb - self.Fp * self.Ixp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                (self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno))) * self.Xbh

        DSndDT = (-self.Ka * self.Snd + self.Kh * ((self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno)))) * self.Xbh

        DSnhDT = (-self.Ixb * self.Uh * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno))) + self.Ka * self.Snd) * self.Xbh - self.Ua * (
                         self.Ixb + 1 / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                         self.So / (self.Koa + self.So)) * self.Xba

        DSnoDT = -self.Uh * self.Ng * ((1 - self.Yh) / (2.86 * self.Yh)) * (self.Ss / (self.Ks + self.Ss)) * (
                self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno)) * self.Xbh + (
                         self.Ua / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                         self.So / (self.Koa + self.So)) * self.Xba

        DSoDT = -self.Uh * ((1 - self.Yh) / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                self.So / (self.Koh + self.So)) * self.Xbh - self.Ua * ((4.57 - self.Ya) / self.Ya) * (
                        self.Snh / (self.Knh + self.Snh)) * (self.So / (self.Koa + self.So)) * self.Xba

        return [DXbhDT, DXbaDT, DSsDT, DXsDT, DXpDT, DXndDT, DSndDT, DSnhDT, DSnoDT, DSoDT]

    def odesolve(self):
        uzero = [self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So]
        solution = odeint(self.equationss, uzero, self.t)
        return solution

    def rownania(self):
        r = self.odesolve()
        self.Xbh1 = r[1][0]
        self.Xba1 = r[1][1]
        self.Ss1 = r[1][2]
        self.Xs1 = r[1][3]
        self.Xp1 = r[1][4]
        self.Xnd1 = r[1][5]
        self.Snd1 = r[1][6]
        self.Snh1 = r[1][7]
        self.Sno1 = r[1][8]
        self.So1 = r[1][9]
        return self.Xbh1, self.Xba1, self.Ss1, self.Xs1, self.Xp1, self.Xnd1, self.Snd1, self.Snh1, self.Sno1, self.So1

    def graphs(i):
        data = pd.read_csv('data.csv')
        x = data['t']
        y1 = data['Xbh']
        y2 = data['Xba']
        y3 = data['Ss']
        y4 = data['Xs']
        y5 = data['Xp']
        y6 = data['Xnd']
        y7 = data['Snd']
        y8 = data['Snh']
        y9 = data['Sno']
        y10 = data['So']

        plt.cla()
        plt.plot(x, y1, label='Xbh')
        plt.plot(x, y2, label='Xba')
        plt.plot(x, y3, label='Ss')
        plt.plot(x, y4, label='Xs')
        plt.plot(x, y5, label='Xp')
        plt.plot(x, y6, label='Xnd')
        plt.plot(x, y7, label='Snd')
        plt.plot(x, y8, label='Snh')
        plt.plot(x, y9, label='Sno')
        plt.plot(x, y10, label='So')
        plt.legend(loc='upper left')
        plt.gca().xaxis.set_major_locator(mticker.MaxNLocator())
        plt.tight_layout()

    def __iter__(self):
        return

    def __next__(self):
        rown = self.rownania()
        self.Xbh = rown[0]
        self.Xba = rown[1]
        self.Ss = rown[2]
        self.Xs = rown[3]
        self.Xp = rown[4]
        self.Xnd = rown[5]
        self.Snd = rown[6]
        self.Snh = rown[7]
        self.Sno = rown[8]
        self.So = rown[9]
        return self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So

# x = reactor_ASM1()
# Uzero = [x.Xbh, x.Xba, x.Ss, x.Xs, x.Xp, x.Xnd, x.Snd, x.Snh, x.Sno, x.So]

# y = reactor_ASM1().odesolve()
# print(y)
# print(y[1][0])
# plt.plot(x.t, y[:, 0])
# plt.plot(x.t, y[:, 1])
# plt.plot(x.t, y[:, 2])
# plt.plot(x.t, y[:, 3])
# plt.plot(x.t, y[:, 4])
# plt.plot(x.t, y[:, 5])
# plt.plot(x.t, y[:, 6])
# plt.plot(x.t, y[:, 7])
# plt.plot(x.t, y[:, 8])
# plt.plot(x.t, y[:, 9])
# plt.show()
# print(y)
