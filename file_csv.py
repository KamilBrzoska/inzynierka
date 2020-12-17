from test import reactor_ASM1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation
import csv

model = reactor_ASM1()
#model.rownania()

fieldnames = ["Xbh", "Xba", "Ss", "Xs", "Xp", "Xnd", "Snd", "Snh", "Sno", "So", "t"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        Xbh = next(model)[0]
        Xba = next(model)[1]
        Ss = next(model)[2]
        Xs = next(model)[3]
        Xp = next(model)[4]
        Xnd = next(model)[5]
        Snd = next(model)[6]
        Snh = next(model)[7]
        Sno = next(model)[8]
        So = next(model)[9]
        x1 = model.t[-1]
        x1 += 1
        model.t[-1] = x1


        info = {
            "Xbh": Xbh,
            "Xba": Xba,
            "Ss": Ss,
            "Xs": Xs,
            "Xp": Xp,
            "Xnd": Xnd,
            "Snd": Snd,
            "Snh": Snh,
            "Sno": Sno,
            "So": So,
            "t": model.t,
        }

        csv_writer.writerow(info)
        print(Xbh, Xba, Ss, Xs, Xp, Xnd, Snd, Snh, Sno, So, model.t)

    time.sleep(1)
