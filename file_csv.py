import test
import time
import csv
import os
import atexit

model = test.Settler()

def exit_handler():
    try:
        os.remove("data.csv")
    except FileNotFoundError:
        print("plik z danymi zostal usuniety")


only_for_close_function = True


def makesimulation(add_time,add_time1):
    fieldnames = ["Xbh", "Xba", "Ss", "Xs", "Xp", "Xnd", "Snd", "Snh", "Sno", "So", "t"]
    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while only_for_close_function:
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
            x1 += add_time
            x1 = round(x1, 1)
            model.t[-1] = x1

            x0 = model.t[0]
            x0 += add_time1
            x0 = round(x0, 1)
            model.t[0] = x0


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
                "t": model.t[-1],
            }
            csv_writer.writerow(info)

            # do sprawdzenia osadnika
            s0 = Step[10]
            s1 = Step[11]
            s2 = Step[12]
            s3 = Step[13]
            s4 = Step[14]
            s5 = Step[15]
            s6 = Step[16]
            s7 = Step[17]
            s8 = Step[18]
            s9 = Step[19]
            print(s0, s1, s2, s3, s4, s5, s6, s7, s8, s9)
            # koniec sprawdzenia osadnka
            # wlaczyc tego printa zeby pokazywalo stezenia z reaktora
            # print(Xbh, Xba, Ss, Xs, Xp, Xnd, Snd, Snh, Sno, So, model.t)

        time.sleep(1)

atexit.register(exit_handler)
