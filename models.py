import numpy as np
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker
from math import e
from mpl_toolkits import mplot3d

class Reactor:

    def __init__(self):
        # parametry początkowe
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

        # dopływ
        self.Xsd = 0.1
        self.Xpd = 0.2
        self.Xndd = 0.001
        self.Ssd = 0.32
        self.Sndd = 0.002
        self.Snhd = 0.9
        self.Snod = 0.0
        self.Sod = 0.0
        self.Qd = 5  # natężenie przepływu w dopływie

        # pozostałe parametry
        self.Uh = 6.98  #
        self.Ks = 0.3  #
        self.Koh = 0.156  #
        self.Ng = 0.5  #
        self.Kno = 0.1  #
        self.Bh = 0.62  #
        self.Ua = 2.0  #
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
        self.V = 100  # objętośc reaktora
        self.Qw = self.Qd
        self.kla = 0.05
        # self.n = 0.1
        # self.t = np.linspace(0, self.n, 10)

    def equationss(self, U, t):
        self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So = U
        dxbh_dt = ((self.Uh * self.Ss) / (self.Ks + self.Ss)) * (
                (self.Xbh * self.So) / (self.Koh + self.So)) + self.Ng * self.Uh * (
                          self.Ss / (self.Ks + self.Ss)) * (
                          self.Koh / (self.Koh + self.So)) * (
                          self.Sno / (self.Kno + self.Sno)) * self.Xbh - self.Bh * self.Xbh

        dxba_dt = self.Ua * (self.Snh / (self.Knh + self.Snh)) * (
                self.So / (self.Koa + self.So)) * self.Xba - self.Ba * self.Xba

        dss_dt = ((-self.Uh / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno))) + self.Kh * (
                          (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                          (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                          self.Sno / (self.Kno + self.Sno)))) * self.Xbh

        dxs_dt = (1 - self.Fp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                         self.Sno / (self.Kno + self.Sno))) * self.Xbh

        dxp_dt = self.Fp * (self.Bh * self.Xbh + self.Ba * self.Xba)

        dxnd_dt = (self.Ixb - self.Fp * self.Ixp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                (self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                          (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                          self.Sno / (self.Kno + self.Sno))) * self.Xbh

        dsnd_dt = (-self.Ka * self.Snd + self.Kh * ((self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno)))) * self.Xbh

        dsnh_dt = (-self.Ixb * self.Uh * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                self.Sno / (self.Kno + self.Sno))) + self.Ka * self.Snd) * self.Xbh - self.Ua * (
                          self.Ixb + 1 / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                          self.So / (self.Koa + self.So)) * self.Xba

        dsno_dt = -self.Uh * self.Ng * ((1 - self.Yh) / (2.86 * self.Yh)) * (self.Ss / (self.Ks + self.Ss)) * (
                self.Koh / (self.Koh + self.So)) * (
                          self.Sno / (self.Kno + self.Sno)) * self.Xbh + (
                          self.Ua / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                          self.So / (self.Koa + self.So)) * self.Xba

        dso_dt = -self.Uh * ((1 - self.Yh) / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                self.So / (self.Koh + self.So)) * self.Xbh - self.Ua * ((4.57 - self.Ya) / self.Ya) * (
                         self.Snh / (self.Knh + self.Snh)) * (self.So / (self.Koa + self.So)) * self.Xba + self.kla \
                 * (10 - self.So)

        return [dxbh_dt, dxba_dt, dss_dt, dxs_dt, dxp_dt, dxnd_dt, dsnd_dt, dsnh_dt, dsno_dt, dso_dt]

    def odesolve(self):
        uzero = [self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So]
        solution = odeint(self.equationss, uzero, self.t)
        return solution

    def rownania(self):
        r = self.odesolve()
        xbh1 = r[1][0]
        xba1 = r[1][1]
        ss1 = r[1][2]
        xs1 = r[1][3]
        xp1 = r[1][4]
        xnd1 = r[1][5]
        snd1 = r[1][6]
        snh1 = r[1][7]
        sno1 = r[1][8]
        so1 = r[1][9]
        return xbh1, xba1, ss1, xs1, xp1, xnd1, snd1, snh1, sno1, so1

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


class Settler(Reactor):
    def __init__(self):
        super().__init__()
        self.n = 10
        self.w = 7
        # generowanie losowych wartości X dla każdej warstwy
        self.i = 0
        self.Xin = self.Xbh + self.Xba + self.Xs + self.Xp + self.Xnd

        self.nv = 10
        self.Qin = self.Qw
        self.Qcl = 0.3 * self.Qin
        self.Qth = 0.7 * self.Qin
        self.A = 5
        self.H = 100
        self.v0 = 10
        self.X1 = 0
        self.X2 = 0
        self.X3 = 0
        self.X4 = 0
        self.X5 = 0
        self.X6 = 0
        self.X7 = 0
        self.X8 = 0
        self.X9 = 0
        self.X10 = 0

        # recykl
        self.Xbhw = 0
        self.Xbaw = 0
        self.Xsw = 0
        self.Xpw = 0
        self.Xndw = 0

    def graphs_settler(i):
        data = pd.read_csv('data.csv')

        ax = plt.axes(projection='3d')

        z=np.array([data['layer1'], data['layer2'], data['layer3'], data['layer4'], data['layer5'], data['layer6'],
                    data['layer7'], data['layer8'], data['layer9'], data['layer10']])
        x=data['t']
        y=np.array([data['1'], data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'],
                    data['9'], data['10']])

        ax.plot_surface(x,y,z)
        ax.mouse_init()



        #kilka kresek

        # ax = plt.axes(projection='3d')
        # zline1 = data["layer1"]
        # xline1 = data['1']
        # yline1 = data['t']
        #
        # zline2 = data["layer2"]
        # xline2 = data['2']
        # yline2 = data['t']
        #
        # zline3 = data["layer3"]
        # xline3 = data['3']
        # yline3 = data['t']
        #
        # zline4 = data["layer4"]
        # xline4 = data['4']
        # yline4 = data['t']
        #
        # zline5 = data["layer5"]
        # xline5 = data['5']
        # yline5 = data['t']
        #
        # zline6 = data["layer6"]
        # xline6 = data['6']
        # yline6 = data['t']
        #
        # zline7 = data["layer7"]
        # xline7 = data['7']
        # yline7 = data['t']
        #
        # zline8 = data["layer8"]
        # xline8 = data['8']
        # yline8 = data['t']
        #
        # zline9 = data["layer9"]
        # xline9 = data['9']
        # yline9 = data['t']
        #
        # zline10 = data["layer10"]
        # xline10 = data['10']
        # yline10 = data['t']
        #
        # ax.plot3D(xline1, yline1, zline1, label='warstwa1')
        # ax.plot3D(xline2, yline2, zline2, label='warstwa2')
        # ax.plot3D(xline3, yline3, zline3, label='warstwa3')
        # ax.plot3D(xline4, yline4, zline4, label='warstwa4')
        # ax.plot3D(xline5, yline5, zline5, label='warstwa5')
        # ax.plot3D(xline6, yline6, zline6, label='warstwa6')
        # ax.plot3D(xline7, yline7, zline7, label='warstwa7')
        # ax.plot3D(xline8, yline8, zline8, label='warstwa8')
        # ax.plot3D(xline9, yline9, zline9, label='warstwa9')
        # ax.plot3D(xline10, yline10, zline10, label='warstwa10')

        #stare

        # x = data['t']
        # y1 = data['layer1']
        # y2 = data['layer2']
        # y3 = data['layer3']
        # y4 = data['layer4']
        # y5 = data['layer5']
        # y6 = data['layer6']
        # y7 = data['layer7']
        # y8 = data['layer8']
        # y9 = data['layer9']
        # y10 = data['layer10']
        #
        # plt.cla()
        # plt.plot(x, y1, label='warstwa 1')
        # plt.plot(x, y2, label='warstwa 2')
        # plt.plot(x, y3, label='warstwa 3')
        # plt.plot(x, y4, label='warstwa 4')
        # plt.plot(x, y5, label='warstwa 5')
        # plt.plot(x, y6, label='warstwa 6')
        # plt.plot(x, y7, label='warstwa 7')
        # plt.plot(x, y8, label='warstwa 8')
        # plt.plot(x, y9, label='warstwa 9')
        # plt.plot(x, y10, label='warstwa 10')
        plt.legend(loc='upper left')
        plt.gca().xaxis.set_major_locator(mticker.MaxNLocator())
        plt.tight_layout()

    # funkcje prędkości sedymentacji
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

    # strumienie masy pochodzące od przepływu wody
    def jup1(self):
        j_up1 = (self.Qcl * self.X1) / self.A
        j_up2 = (self.Qcl * self.X2) / self.A
        j_up3 = (self.Qcl * self.X3) / self.A
        j_up4 = (self.Qcl * self.X4) / self.A
        j_up5 = (self.Qcl * self.X5) / self.A
        j_up6 = (self.Qcl * self.X6) / self.A
        j_up7 = (self.Qcl * self.X7) / self.A
        j_dn7 = (self.Qth * self.X7) / self.A
        j_dn8 = (self.Qth * self.X8) / self.A
        j_dn9 = (self.Qth * self.X9) / self.A
        j_dn10 = (self.Qth * self.X10) / self.A
        return j_up1, j_up2, j_up3, j_up4, j_up5, j_up6, j_up7, j_dn7, j_dn8, j_dn9, j_dn10

    # strumienie masy pochodzące od sedymentacji
    def js1(self):
        vs = self.vs1()
        js1 = min(vs[0] * self.X1, vs[1] * self.X2)
        js2 = min(vs[1] * self.X2, vs[2] * self.X3)
        js3 = min(vs[2] * self.X3, vs[3] * self.X4)
        js4 = min(vs[3] * self.X4, vs[4] * self.X5)
        js5 = min(vs[4] * self.X5, vs[5] * self.X6)
        js6 = min(vs[5] * self.X6, vs[6] * self.X7)
        js7 = min(vs[6] * self.X7, vs[7] * self.X8)
        js8 = min(vs[7] * self.X8, vs[8] * self.X9)
        js9 = min(vs[8] * self.X9, vs[9] * self.X10)
        return js1, js2, js3, js4, js5, js6, js7, js8, js9

    # równania różniczkowe zwyczajne
    # warstwa górna
    def dxdt(self, u1, t, jup, js):
        self.X1, self.X2, self.X3, self.X4, self.X5, self.X6, self.X7, self.X8, self.X9, self.X10 = u1

        dx1_dt = (self.n / self.H) * (jup[1] - js[0] - ((self.Qcl * self.X1) / self.A))
        # warstwy powyżej wejściowej
        dx2_dt = (self.n / self.H) * (jup[2] - jup[1] + js[0] - js[1])
        dx3_dt = (self.n / self.H) * (jup[3] - jup[2] + js[1] - js[2])
        dx4_dt = (self.n / self.H) * (jup[4] - jup[3] + js[2] - js[3])
        dx5_dt = (self.n / self.H) * (jup[5] - jup[4] + js[3] - js[4])
        dx6_dt = (self.n / self.H) * (jup[6] - jup[5] + js[4] - js[5])
        # warstwa wejściowa
        dx7_dt = (self.n / self.H) * (-jup[6] - jup[7] + js[5] - js[6] + ((self.Qin * self.Xin) / self.A))
        # warstwy poniżej wejściowej
        dx8_dt = (self.n / self.H) * (jup[7] - jup[8] + js[6] - js[7])
        dx9_dt = (self.n / self.H) * (jup[8] - jup[9] + js[7] - js[8])
        # warstwa dolna
        dx10_dt = (self.n / self.H) * (jup[9] + js[8] - ((self.Qth * self.X10) / self.A))
        return [dx1_dt, dx2_dt, dx3_dt, dx4_dt, dx5_dt, dx6_dt, dx7_dt, dx8_dt, dx9_dt, dx10_dt]

    def odesolve_settler(self):
        jup = self.jup1()
        js = self.js1()
        uzero1 = [self.X1, self.X2, self.X3, self.X4, self.X5, self.X6, self.X7, self.X8, self.X9, self.X10]
        solution1 = odeint(self.dxdt, uzero1, self.t, args=(jup, js))
        return solution1

    def recykl(self):
        rec = (self.Qth * self.X10) / self.A
        if rec == 0:
            pass
        else:
            self.Xbhw = self.Xbh * (rec / self.Xin)
            self.Xbaw = self.Xba * (rec / self.Xin)
            self.Xsw = self.Xs * (rec / self.Xin)
            self.Xpw = self.Xp * (rec / self.Xin)
            self.Xndw = self.Xnd * (rec / self.Xin)
        return rec, self.Xbhw, self.Xbaw, self.Xsw, self.Xpw, self.Xndw

    def masa(self):
        recykl = self.recykl()
        rownania = self.rownania()
        xbh2 = ((rownania[0] * self.V) + recykl[1] - (rownania[0] * self.Qw)) / self.V
        xba2 = ((rownania[1] * self.V) + recykl[2] - (rownania[1] * self.Qw)) / self.V
        ss2 = ((rownania[2] * self.V) + (self.Ssd * self.Qd) - (rownania[2] * self.Qw)) / self.V
        xs2 = ((rownania[3] * self.V) + recykl[3] + (self.Xsd * self.Qd) - (rownania[3] * self.Qw)) / self.V
        xp2 = ((rownania[4] * self.V) + recykl[4] + (self.Xpd * self.Qd) - (rownania[4] * self.Qw)) / self.V
        xnd2 = ((rownania[5] * self.V) + recykl[5] + (self.Xndd * self.Qd) - (rownania[5] * self.Qw)) / self.V
        snd2 = ((rownania[6] * self.V) + (self.Sndd * self.Qd) - (rownania[6] * self.Qw)) / self.V
        snh2 = ((rownania[7] * self.V) + (self.Snhd * self.Qd) - (rownania[7] * self.Qw)) / self.V
        sno2 = ((rownania[8] * self.V) + (self.Snod * self.Qd) - (rownania[8] * self.Qw)) / self.V
        so2 = ((rownania[9] * self.V) + (self.Sod * self.Qd) - (rownania[9] * self.Qw)) / self.V
        return [xbh2, xba2, ss2, xs2, xp2, xnd2, snd2, snh2, sno2, so2]

    def __iter__(self):
        return

    def __next__(self):
        rown = self.masa()
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

        solv = self.odesolve_settler()
        self.X1 = solv[1][0]
        self.X2 = solv[1][1]
        self.X3 = solv[1][2]
        self.X4 = solv[1][3]
        self.X5 = solv[1][4]
        self.X6 = solv[1][5]
        self.X7 = solv[1][6]
        self.X8 = solv[1][7]
        self.X9 = solv[1][8]
        self.X10 = solv[1][9]
        return self.Xbh, self.Xba, self.Ss, self.Xs, self.Xp, self.Xnd, self.Snd, self.Snh, self.Sno, self.So, \
               self.X1, self.X2, self.X3, self.X4, self.X5, self.X6, self.X7, self.X8, self.X9, self.X10
