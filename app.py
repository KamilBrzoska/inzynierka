import os
import subprocess
from tkinter import *

from matplotlib.figure import Figure

from test import reactor_ASM1
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import file_csv
import _thread
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# from tkinter.ttk import Notebook
reactor = reactor_ASM1()


# window = Tk()
# window.title("Simulator")


class Simulator:
    def __init__(self, master):
        self.master = master
        master.title("Symulator")

        # frame
        main_frame = Frame(window, width=150, height=370, bg='grey')
        main_frame.pack(side='left', fill='both', padx=10, pady=5)

        left_frame = Frame(main_frame, width=90, height=185, bg='grey')
        left_frame.pack(side='left', fill='both', padx=10, pady=5, expand=True)

        right_frame = Frame(main_frame, width=90, height=185, bg='grey')
        right_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)

        self.graph_frame = Frame(window, width=400, height=400, bg='grey')
        self.graph_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)

        # graph frame

        # inital values

        self.entry_value_xbh = DoubleVar(right_frame, value=reactor.Xbh)
        self.enter_xbh = Entry(right_frame, textvariable=self.entry_value_xbh).pack(padx=5, pady=5)

        self.entry_value_xba = DoubleVar(right_frame, value=reactor.Xba)
        self.enter_xba = Entry(right_frame, textvariable=self.entry_value_xba).pack(padx=5, pady=5)

        self.entry_value_ss = DoubleVar(right_frame, value=reactor.Ss)
        self.enter_ss = Entry(right_frame, textvariable=self.entry_value_ss).pack(padx=5, pady=5)

        self.entry_value_xs = DoubleVar(right_frame, value=reactor.Xs)
        self.enter_xs = Entry(right_frame, textvariable=self.entry_value_xs).pack(padx=5, pady=5)

        self.entry_value_xp = DoubleVar(right_frame, value=reactor.Xp)
        self.enter_xp = Entry(right_frame, textvariable=self.entry_value_xp).pack(padx=5, pady=5)

        self.entry_value_xnd = DoubleVar(right_frame, value=reactor.Xnd)
        self.enter_xnd = Entry(right_frame, textvariable=self.entry_value_xnd).pack(padx=5, pady=5)

        self.entry_value_snd = DoubleVar(right_frame, value=reactor.Snd)
        self.enter_snd = Entry(right_frame, textvariable=self.entry_value_snd).pack(padx=5, pady=5)

        self.entry_value_snh = DoubleVar(right_frame, value=reactor.Snh)
        self.enter_snh = Entry(right_frame, textvariable=self.entry_value_snh).pack(padx=5, pady=5)

        self.entry_value_sno = DoubleVar(right_frame, value=reactor.Sno)
        self.enter_sno = Entry(right_frame, textvariable=self.entry_value_sno).pack(padx=5, pady=5)

        self.entry_value_so = DoubleVar(right_frame, value=reactor.So)
        self.enter_so = Entry(right_frame, textvariable=self.entry_value_so).pack(padx=5, pady=5)

        # Labels
        define = Frame(left_frame, width=90, height=185)
        define.pack(side='left', fill='both', padx=5, pady=5, expand=True)

        # Label(define, text='Symulator', bg="black", fg="white", font="none 12 bold").pack()
        Label(define, text="Xbh", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="Xba", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="Ss", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="Xs", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="Xp", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="Xnd", font="none 12 bold").pack(padx=5, pady=8)
        Label(define, text="Snd", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="Snh", font="none 12 bold").pack(padx=5, pady=8)
        Label(define, text="Sno", font="none 12 bold").pack(padx=5, pady=7)
        Label(define, text="So", font="none 12 bold").pack(padx=5, pady=7)

        # graph
        self.x = reactor_ASM1.graphs
        self.figure1 = plt.gcf()
        self.canvas = FigureCanvasTkAgg(self.figure1, master=self.graph_frame)

        # Buttons
        Button(right_frame, text="Rozpocznij symulacje", width="15", command=lambda: self.start_simulation()).pack(
            side='bottom', padx=5, pady=5)
        Button(right_frame, text="Pokaż wykres", width="15", command=lambda: self.obrazek()).pack(side='bottom', padx=5,
                                                                                                  pady=5)
        Button(right_frame, text="Wyzeruj", width="15", command=lambda: self.wyzeruj()).pack(
            side='bottom', padx=5,
            pady=5)

    def start_simulation(self):
        if os.path.isfile("data.csv"):
            print ("Najpierw zakoncz poprzednia symulacje")
        else:
            file_csv.only_for_close_function = True
            _thread.start_new_thread(file_csv.makesimulation, ())

            xbh1 = float(self.entry_value_xbh.get())
            file_csv.model.Xbh = xbh1

            xba1 = float(self.entry_value_xba.get())
            file_csv.model.Xba = xba1

            ss1 = float(self.entry_value_ss.get())
            file_csv.model.Ss = ss1

            xs1 = float(self.entry_value_xs.get())
            file_csv.model.Xs = xs1

            xp1 = float(self.entry_value_xp.get())
            file_csv.model.Xp = xp1

            xnd1 = float(self.entry_value_xnd.get())
            file_csv.model.Xnd = xnd1

            xbh1 = float(self.entry_value_xbh.get())
            file_csv.model.Xbh = xbh1

            snd1 = float(self.entry_value_snd.get())
            file_csv.model.Snd = snd1

            snh1 = float(self.entry_value_snh.get())
            file_csv.model.Snh = snh1

            sno1 = float(self.entry_value_sno.get())
            file_csv.model.Sno = sno1

            so1 = float(self.entry_value_so.get())
            file_csv.model.So = so1
    def obrazek(self):
        self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
        ani = FuncAnimation(plt.gcf(), self.x, interval=1000)
        self.canvas.draw()



    def wyzeruj(self):
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().pack_forget()
        # self.obrazek().plt.clf()
        file_csv.only_for_close_function = False
        if os.path.isfile("data.csv"):
            os.remove("data.csv")
        else:
            print("symulacja zostala juz zakonczona")



window = Tk()
window.maxsize(1200, 700)
window.configure(background="black")
gui = Simulator(window)
window.mainloop()

# window.protocol("WM_DELETE_WINDOW", on_closing)


# def on_closing():
#     messagebox.askokcancel(title="hello", message="hello")
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         window.destroy()
