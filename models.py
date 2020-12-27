import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time


class reactor_ASM1:
    def __init__(self):
        self.Xbh = 1
        self.Xba = 1
        self.Ss = 2
        self.Xs = 1
        self.Xp = 2
        self.Xnd = 20
        self.Snd = 0.2
        self.Snh = 0.8
        self.Sno = 0.5
        self.So = 0.5

        #
        self.Uh = 2  #
        self.Ks = 20  #
        self.Koh = 0.2  #
        self.Ng = 0.8  #
        self.Kno = 0.5  #
        self.Bh = 0.4  #
        self.Ua = 1  #
        self.Knh = 0.01  #
        self.Koa = 0.4  #
        self.Ba = 0.15  #
        self.Kh = 3  #
        self.Yh = 0.54  #
        self.Kx = 0.03  #
        self.Nh = 0.4  #
        self.Fp = 0.08  #
        self.Ixb = 0.086  #
        self.Ka = 0.08  #
        self.Ya = 0.24  #
        self.Ixp = 0.06  #
        self.t = [1]

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
        return (DXbaDT)

    def equation3(self, Ss, t):
        DSsDT = ((-self.Uh / self.Yh) * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                    self.Sno / (self.Kno + self.Sno))) + self.Kh * (
                         (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                             self.Sno / (self.Kno + self.Sno)))) * self.Xbh  # nie jestem pewny
        return (DSsDT)

    def equation4(self, Xs, t):
        DXsDT = (1 - self.Fp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                    (self.Xs / self.Xbh) / (self.Kx + (self.Xs / self.Xbh))) * (
                        (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                            self.Sno / (self.Kno + self.Sno))) * self.Xbh
        return (DXsDT)

    def equation5(self, Xp, t):
        DXpDT = self.Fp * (self.Bh * self.Xbh + self.Ba * self.Xba)
        return (DXpDT)

    def equation6(self, Xnd, t):
        DXndDT = (self.Ixb - self.Fp * self.Ixp) * (self.Bh * self.Xbh + self.Ba * self.Xba) - self.Kh * (
                    (self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                         (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                             self.Sno / (self.Kno + self.Sno))) * self.Xbh  # poprawione
        return (DXndDT)

    def equation7(self, Snd, t):
        DSndDT = (-self.Ka * self.Snd + self.Kh * ((self.Xnd / self.Xbh) / (self.Kx + (self.Xs / self.Bh))) * (
                (self.So / (self.Koh + self.So)) + self.Nh * (self.Koh / (self.Koh + self.So)) * (
                    self.Sno / (self.Kno + self.Sno)))) * self.Xbh
        return (DSndDT)

    def equation8(self, Snh, t):
        DSnhDT = (-self.Ixb * self.Uh * (self.Ss / (self.Ks + self.Ss)) * (
                (self.So / (self.Koh + self.So)) + self.Ng * (self.Koh / (self.Koh + self.So)) * (
                    self.Sno / (self.Kno + self.Sno))) + self.Ka * self.Snd) * self.Xbh - self.Ua * (
                         self.Ixb + 1 / self.Ya) * (self.Snh / (self.Knh + self.Snh)) * (
                             self.So / (self.Koa + self.So)) * self.Xba
        return (DSnhDT)

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
        return self.Xbh1


    def __iter__(self):
        return self

    def __next__(self):
        self.t[0] += 1
        self.Xbh = self.Xbh1
        self.Xba = self.Xba1
        self.Ss = self.Ss1
        self.Xs = self.Xs1
        self.Xp = self.Xp1
        self.Xnd = self.Xnd1
        self.Snd = self.Snd1
        self.Snh = self.Snh1
        self.Sno = self.Sno1
        self.So = self.So1
        return self.rownania, self.t

x = reactor_ASM1()
x1 = x.rownania()
print(x1)

#print(next(x))

#while True:
 #   try:
  #      item = next(x)
   #     print(item)
    #    print(item.rownania.self.Xbh)
       # plt.plot(item[0],item[1])
        #plt.show()
   # except StopIteration:
    #    break




# x0 = [1e6, 9, 100]
# t = np.linspace(0, 15, 1000)
# x = odeint(equation1, x0, t)

# a = x[0:, 0]
# b = x[0:, 1]
# c = x[0:, 2]

# plt.semilogy(t, a)
# plt.semilogy(t, b)
# plt.semilogy(t, c)
# plt.show()
