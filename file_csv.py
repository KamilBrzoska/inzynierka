import sys
from test import reactor_ASM1
import time
import csv
import os
import matplotlib.image as mpimg
import atexit
import numpy as np

model = reactor_ASM1()

def exit_handler():
    os.remove("data.csv")

def makesimulation():
    fieldnames = ["Xbh", "Xba", "Ss", "Xs", "Xp", "Xnd", "Snd", "Snh", "Sno", "So", "t"]

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    try:
        while True:
            with open('data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                Step = next(model)
                Xbh = Step[0]
                Xba = Step[1]
                Ss = Step[2]
                Xs = Step[3]
                Xp = Step[4]
                Xnd = Step[5]
                Snd = Step[6]
                Snh = Step[7]
                Sno = Step[8]
                So = Step[9]
                x1 = model.t[-1]
                x1 += 0.10
                x1=round(x1,1)
                model.t[-1] = x1

                x0 = model.t[0]
                x0 += 0.10
                x0=round(x0,1)
                model.t[0] = x0


                # x1 = model.t[-1]
                # x1 += 0.1
                # x1 = round(x1, 1)
                # model.t.append(x1)


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
            # if Xnd >= 200:
            #     img = mpimg.imread('livelong.jpeg')
            #     imgplot = plt.imshow(img)
            #     plt.show()
            atexit.register(exit_handler)
    except KeyboardInterrupt:
        os.remove("data.csv")
        # ask = input('czy chcesz zapisac dane? (tak/nie): ')
        # if ask == 'nie':
        #     os.remove("data.csv")
        #     print("File Removed!")
        # else:
        #     print("File Saved!")
        #     sys.exit()


# makesimulation()