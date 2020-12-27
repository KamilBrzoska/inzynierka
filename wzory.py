n = int(input("Wprowadź liczbę warstw: "))
w = int(input("Która warstwa ma być wejściową? "))
i = 1
X1 = 100
Qcl = 30
Qin = 100
Qth = 70
H = 100
Jup2 = 50
Js1 = 30
A = 50
wzory = ['']

while i <= n:
    if i == 1:
        wzory.insert(i,
                     "dX" + str(i) + "/dt = " + str(n) + "/H*(Jup" + str(i + 1) + " - Js" + str(i) + " - Qcl * X" + str(
                         i) + " / A)")
        print("dX" + str(i) + "/dt = " + str(n) + "/H*(Jup" + str(i + 1) + " - Js" + str(i) + " - Qcl * X" + str(
            i) + " / A)")
        i += 1
    elif i < w:
        wzory.insert(i, "dX" + str(i) + "/dt = " + str(n) + "/H*(Jup" + str(i + 1) + " - Jup" + str(i) + " + Js" + str(
            i - 1) + " - Js" + str(i) + ")")
        print("dX" + str(i) + "/dt = " + str(n) + "/H*(Jup" + str(i + 1) + " - Jup" + str(i) + " + Js" + str(
            i - 1) + " - Js" + str(i) + ")")
        i += 1
    elif i == w:
        wzory.insert(i, "dX" + str(w) + "/dt = " + str(n) + "/H*(-Jup" + str(w) + " - Jdn" + str(w) + " + Js" + str(
            w - 1) + " - Js" + str(w) + " + Qin * Xin / A)")
        print("dX" + str(w) + "/dt = " + str(n) + "/H*(-Jup" + str(w) + " - Jdn" + str(w) + " + Js" + str(
            w - 1) + " - Js" + str(w) + " + Qin * Xin / A)")
        i += 1
    elif i < n:
        wzory.insert(i, "dX" + str(i) + "/dt = " + str(n) + "/H*(Jdn" + str(i - 1) + " - Jdn" + str(i) + " + Js" + str(
            i - 1) + " - Js" + str(i) + ")")
        print("dX" + str(i) + "/dt = " + str(n) + "/H*(Jdn" + str(i - 1) + " - Jdn" + str(i) + " + Js" + str(
            i - 1) + " - Js" + str(i) + ")")
        i += 1
    else:
        wzory.insert(i, "dX" + str(i) + "/dt = " + str(n) + "/H*(Jdn" + str(i - 1) + " + Js" + str(
            i - 1) + " - Qth * X" + str(i) + " / A)")
        print("dX" + str(i) + "/dt = " + str(n) + "/H*(Jdn" + str(i - 1) + " + Js" + str(i - 1) + " - Qth * X" + str(
            i) + " / A)")
        break

