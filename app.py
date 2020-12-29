from tkinter import *
from test import reactor_ASM1
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import file_csv
import _thread
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

reactor = reactor_ASM1()

window = Tk()
window.title("Simulator")
window.configure(background="black")


def start_simulation():
    _thread.start_new_thread(file_csv.makesimulation, ())
    xbh1 = float(entry_value_xbh.get())
    file_csv.model.Xbh = xbh1

    xba1 = float(entry_value_xba.get())
    file_csv.model.Xba = xba1

    ss1 = float(entry_value_ss.get())
    file_csv.model.Ss = ss1

    xs1 = float(entry_value_xs.get())
    file_csv.model.Xs = xs1

    xp1 = float(entry_value_xp.get())
    file_csv.model.Xp = xp1

    xnd1 = float(entry_value_xnd.get())
    file_csv.model.Xnd = xnd1

    xbh1 = float(entry_value_xbh.get())
    file_csv.model.Xbh = xbh1

    snd1 = float(entry_value_snd.get())
    file_csv.model.Snd = snd1

    snh1 = float(entry_value_snh.get())
    file_csv.model.Snh = snh1

    sno1 = float(entry_value_sno.get())
    file_csv.model.Sno = sno1

    so1 = float(entry_value_so.get())
    file_csv.model.So = so1


def obrazek():
    x = reactor_ASM1.graphs
    figure1 = plt.gcf()
    canvas = FigureCanvasTkAgg(figure1, master=window)
    canvas.get_tk_widget().grid(column=5, row=1,sticky=(N, W, E, S),columnspan = 15,rowspan = 15)
    # canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
    ani = FuncAnimation(plt.gcf(), x, interval=1000)
    # canvas.show()
    canvas.draw()


def input_xbh():
    reactor.Xbh = v


# inital values

entry_value_xbh = DoubleVar(window, value=reactor.Xbh)
enter_xbh = Entry(window, textvariable=entry_value_xbh).grid(row=1, column=1, sticky=W)

entry_value_xba = DoubleVar(window, value=reactor.Xba)
enter_xba = Entry(window, textvariable=entry_value_xba).grid(row=2, column=1, sticky=W)

entry_value_ss = DoubleVar(window, value=reactor.Ss)
enter_ss = Entry(window, textvariable=entry_value_ss).grid(row=3, column=1, sticky=W)

entry_value_xs = DoubleVar(window, value=reactor.Xs)
enter_xs = Entry(window, textvariable=entry_value_xs).grid(row=4, column=1, sticky=W)

entry_value_xp = DoubleVar(window, value=reactor.Xp)
enter_xp = Entry(window, textvariable=entry_value_xp).grid(row=5, column=1, sticky=W)

entry_value_xnd = DoubleVar(window, value=reactor.Xnd)
enter_xnd= Entry(window, textvariable=entry_value_xnd).grid(row=6, column=1, sticky=W)

entry_value_snd = DoubleVar(window, value=reactor.Snd)
enter_snd = Entry(window, textvariable=entry_value_snd).grid(row=7, column=1, sticky=W)

entry_value_snh = DoubleVar(window, value=reactor.Snh)
enter_snh = Entry(window, textvariable=entry_value_snh).grid(row=8, column=1, sticky=W)

entry_value_sno = DoubleVar(window, value=reactor.Sno)
enter_sno = Entry(window, textvariable=entry_value_sno).grid(row=9, column=1, sticky=W)

entry_value_so = DoubleVar(window, value=reactor.So)
enter_so = Entry(window, textvariable=entry_value_so).grid(row=10, column=1, sticky=W)

#Labels
Label(window, text='Symulator', bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky=W,
                                                                                  columnspan=5)
Label(window, text="Xbh", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)
Label(window, text="Xba", bg="black", fg="white", font="none 12 bold").grid(row=2, column=0, sticky=W)
Label(window, text="Ss", bg="black", fg="white", font="none 12 bold").grid(row=3, column=0, sticky=W)
Label(window, text="Xs", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)
Label(window, text="Xp", bg="black", fg="white", font="none 12 bold").grid(row=5, column=0, sticky=W)
Label(window, text="Xnd", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)
Label(window, text="Snd", bg="black", fg="white", font="none 12 bold").grid(row=7, column=0, sticky=W)
Label(window, text="Snh", bg="black", fg="white", font="none 12 bold").grid(row=8, column=0, sticky=W)
Label(window, text="Sno", bg="black", fg="white", font="none 12 bold").grid(row=9, column=0, sticky=W)
Label(window, text="So", bg="black", fg="white", font="none 12 bold").grid(row=10, column=0, sticky=W)



Button(window, text="Rozpocznij symulacje", width="15", command=lambda: start_simulation()).grid(row=11, column=0,
                                                                                                 sticky=W)
Button(window, text="Pokaż wykres", width="15", command=obrazek).grid(row=12, column=0, sticky=W)

# window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

# def on_closing():
#     messagebox.askokcancel(title="hello", message="hello")
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         window.destroy()
