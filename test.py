import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker
from math import e


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

    def suma(self):
        summ = self.Xbh + self.Xba + self.Xs + self.Xp + self.Xnd
        return summ

    # def __iter__(self):
    #     return
    #
    # def __next__(self):
    #     rown = self.rownania()
    #     self.Xbh = rown[0]
    #     self.Xba = rown[1]
    #     self.Ss = rown[2]
    #     self.Xs = rown[3]
    #     self.Xp = rown[4]
    #     self.Xnd = rown[5]
    #     self.Snd = rown[6]
    #     self.Snh = rown[7]
    #     self.Sno = rown[8]
    #     self.So = rown[9]
    #
    #     return self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So


class Settler(reactor_ASM1):
    def __init__(self):
        super().__init__()
        self.n = 10
        self.w = 7
        # generowanie losowych wartości X dla każdej warstwy
        self.i = 0
        self.Xin = self.Xbh + self.Xba + self.Xs + self.Xp + self.Xnd
        self.X = np.random.random(self.n)
        self.X /= self.X.sum()
        self.X *= self.Xin
        #
        self.nv = 10
        self.Qcl = 30
        self.Qth = 70
        self.Qin = 100
        self.A = 50
        self.H = 100
        self.v0 = 10
        self.X1 = self.X[0]
        self.X2 = self.X[1]
        self.X3 = self.X[2]
        self.X4 = self.X[3]
        self.X5 = self.X[4]
        self.X6 = self.X[5]
        self.X7 = self.X[6]
        self.X8 = self.X[7]
        self.X9 = self.X[8]
        self.X10 = self.X[9]

    ## funkcje prędkości sedymentacji
    def vs1(self):
        vs1 = self.v0 * (e ** (-self.nv * self.X1))
        vs2 = self.v0 * (e ** (-self.nv * self.X2))
        vs3 = self.v0 * (e ** (-self.nv * self.X3))
        vs4 = self.v0 * (e ** (-self.nv * self.X4))
        vs5 = self.v0 * (e ** (-self.nv * self.X5))
        vs6 = self.v0 * (e ** (-self.nv * self.X6))
        vs7 = self.v0 * (e ** (-self.nv * self.X7))
        vs8 = self.v0 * (e ** (-self.nv * self.X8))
        vs9 = self.v0 * (e ** (-self.nv * self.X9))
        vs10 = self.v0 * (e ** (-self.nv * self.X10))
        return vs1, vs2, vs3, vs4, vs5, vs6, vs7, vs8, vs9, vs10

    ## strumienie masy pochodzące od przepływu wody
    def Jup1(self):
        Jup1 = (self.Qcl * self.X1) / self.A
        Jup2 = (self.Qcl * self.X2) / self.A
        Jup3 = (self.Qcl * self.X3) / self.A
        Jup4 = (self.Qcl * self.X4) / self.A
        Jup5 = (self.Qcl * self.X5) / self.A
        Jup6 = (self.Qcl * self.X6) / self.A
        Jup7 = (self.Qcl * self.X7) / self.A
        Jdn7 = (self.Qth * self.X7) / self.A
        Jdn8 = (self.Qth * self.X8) / self.A
        Jdn9 = (self.Qth * self.X9) / self.A
        Jdn10 = (self.Qth * self.X10) / self.A
        return Jup1, Jup2, Jup3, Jup4, Jup5, Jup6, Jup7, Jdn7, Jdn8, Jdn9, Jdn10

    ## strumienie masy pochodzące od sedymentacji
    def Js1(self):
        vs = self.vs1()
        Js1 = min(vs[0] * self.X1, vs[1] * self.X2)
        Js2 = min(vs[1] * self.X2, vs[2] * self.X3)
        Js3 = min(vs[2] * self.X3, vs[3] * self.X4)
        Js4 = min(vs[3] * self.X4, vs[4] * self.X5)
        Js5 = min(vs[4] * self.X5, vs[5] * self.X6)
        Js6 = min(vs[5] * self.X6, vs[6] * self.X7)
        Js7 = min(vs[6] * self.X7, vs[7] * self.X8)
        Js8 = min(vs[7] * self.X8, vs[8] * self.X9)
        Js9 = min(vs[8] * self.X9, vs[9] * self.X10)
        return Js1, Js2, Js3, Js4, Js5, Js6, Js7, Js8, Js9

    ## równania różniczkowe zwyczajne
    # warstwa górna
    def dX1dt(self, u1, t):
        u1 = self.X1, self.X2, self.X3, self.X4, self.X5, self.X6, self.X7, self.X8, self.X9, self.X10
        Jup = self.Jup1()
        Js = self.Js1()
        dX1dt = (self.n / self.H) * (Jup[1] - Js[0] - ((self.Qcl * self.X1) / self.A))
        # warstwy powyżej wejściowej
        dX2dt = (self.n / self.H) * (Jup[2] - Jup[1] + Js[0] - Js[1])
        dX3dt = (self.n / self.H) * (Jup[3] - Jup[2] + Js[1] - Js[2])
        dX4dt = (self.n / self.H) * (Jup[4] - Jup[3] + Js[2] - Js[3])
        dX5dt = (self.n / self.H) * (Jup[5] - Jup[6] + Js[3] - Js[4])
        dX6dt = (self.n / self.H) * (Jup[6] - Jup[5] + Js[4] - Js[5])
        # warstwa wejściowa
        dX7dt = (self.n / self.H) * (-Jup[6] - Jup[7] + Js[5] - Js[6] + ((self.Qin * self.Xin) / self.A))
        # warstwy poniżej wejściowej
        dX8dt = (self.n / self.H) * (Jup[7] - Jup[8] + Js[6] - Js[7])
        dX9dt = (self.n / self.H) * (Jup[8] - Jup[9] + Js[7] - Js[8])
        # warstwa dolna
        dX10dt = (self.n / self.H) * (Jup[9] + Js[8] - ((self.Qth * self.X10) / self.A))
        return dX1dt, dX2dt, dX3dt, dX4dt, dX5dt, dX6dt, dX7dt, dX8dt, dX9dt, dX10dt

    def odesolve_settler(self):
        uzero1 = [self.X1, self.X2, self.X3, self.X4, self.X5, self.X6, self.X7, self.X8, self.X9, self.X10]
        solution1 = odeint(self.dX1dt, uzero1, self.t)
        return solution1

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

        self.Xin = rown[0] + rown[1] + rown[3] + rown[4] + rown[5]
        self.X = np.random.random(self.n)
        self.X /= self.X.sum()
        self.X *= self.Xin

        solv = self.odesolve_settler()
        s0 = solv[1][0]
        s1 = solv[1][1]
        s2 = solv[1][2]
        s3 = solv[1][3]
        s4 = solv[1][4]
        s5 = solv[1][5]
        s6 = solv[1][6]
        s7 = solv[1][7]
        s8 = solv[1][8]
        s9 = solv[1][9]
        return self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So, s0, s1, s2, s3, s4, s5, s6, s7, s8, s9
