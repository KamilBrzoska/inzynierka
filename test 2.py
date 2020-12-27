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

    def equation1(self, Xbh, t):
        DXbhDT = ((self.Uh * self.Ss) / (self.Ks + self.Ss)) * (
                (self.Xbh * self.So) / (self.Koh + self.So)) + self.Ng * self.Uh * (
                         self.Ss / (self.Ks + self.Ss)) * (
                         self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno)) * self.Xbh - self.Bh * self.Xbh
        return DXbhDT

    def equation2(self, Xba, t):
        DXbaDT = self.Ua * (self.Snh / (self.Knh + self.Snh)) * (
                self.So / (self.Koa + self.So)) * self.Xba - self.Ba * self.Xba
        return DXbaDT

    def equation3(self, Ss, t):
        DSsDT = ((-self.Uh / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno))) + self.Kh * (
                         (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno)))) * self.Xbh
        return DSsDT

    def equation4(self, Xs, t):
        DXsDT = (1 - self.Fp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                        (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                        self.Sno / (self.Kno + self.Sno))) * self.Xbh
        return DXsDT

    def equation5(self, Xp, t):
        DXpDT = self.Fp * (self.Bh * self.Xbh + self.Ba * self.Xba)
        return DXpDT

    def equation6(self, Xnd, t):
        DXndDT = (self.Ixb - self.Fp * self.Ixp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                (self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno))) * self.Xbh
        return DXndDT

    def equation7(self, Snd, t):
        DSndDT = (-self.Ka * self.Snd + self.Kh * ((self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno)))) * self.Xbh
        return DSndDT

    def equation8(self, Snh, t):
        DSnhDT = (-self.Ixb * self.Uh * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno))) + self.Ka * self.Snd) * self.Xbh - self.Ua * (
                         self.Ixb + 1 / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                         self.So / (self.Koa + self.So)) * self.Xba
        return DSnhDT

    def equation9(self, Sno, t):
        DSnoDT = -self.Uh * self.Ng * ((1 - self.Yh) / (2.86 * self.Yh)) * (self.Ss / (self.Ks + self.Ss)) * (
                self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno)) * self.Xbh + (
                         self.Ua / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                         self.So / (self.Koa + self.So)) * self.Xba
        return DSnoDT

    def equation10(self, So, t):
        DSoDT = -self.Uh * ((1 - self.Yh) / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                self.So / (self.Koh + self.So)) * self.Xbh - self.Ua * ((4.57 - self.Ya) / self.Ya) * (
                        self.Snh / (self.Knh + self.Snh)) * (self.So / (self.Koa + self.So)) * self.Xba

        return DSoDT

    def rownania(self):
        self.Xbh1 = odeint(self.equation1, self.Xbh, self.t)
        self.Xba1 = odeint(self.equation2, self.Xba, self.t)
        self.Ss1 = odeint(self.equation3, self.Ss, self.t)
        self.Xs1 = odeint(self.equation4, self.Xs, self.t)
        self.Xp1 = odeint(self.equation5, self.Xp, self.t)
        self.Xnd1 = odeint(self.equation6, self.Xnd, self.t)
        self.Snd1 = odeint(self.equation7, self.Snd, self.t)
        self.Snh1 = odeint(self.equation8, self.Snh, self.t)
        self.Sno1 = odeint(self.equation9, self.Sno, self.t)
        self.So1 = odeint(self.equation10, self.So, self.t)
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
        # self.Xbh += 1
        self.Xbh = self.rownania()[0][-1, 0]
        self.Xba = self.rownania()[1][-1, 0]
        self.Ss = self.rownania()[2][-1, 0]
        self.Xs = self.rownania()[3][-1, 0]
        self.Xp = self.rownania()[4][-1, 0]
        self.Xnd = self.rownania()[5][-1, 0]
        self.Snd = self.rownania()[6][-1, 0]
        # self.Snd += 0.05
        self.Snh = self.rownania()[7][-1, 0]
        self.Sno = self.rownania()[8][-1, 0]
        self.So = self.rownania()[9][-1, 0]
        # self.So += 0.00001
        return self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So
