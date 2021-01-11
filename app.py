import os
from tkinter import *

import pandas as pd
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from sympy.physics.quantum.circuitplot import matplotlib

from test import Reactor
from test import Settler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import file_csv
import _thread
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

reactor = Reactor()
settler = Settler()


class Scrollable(Frame):

    def __init__(self, frame, width=16):
        scrollbar = Scrollbar(frame, width=width)
        scrollbar.pack(side='right', fill='y', expand=False)

        self.canvas = Canvas(frame, yscrollcommand=scrollbar.set, width=300)
        self.canvas.pack(side='left', fill='both', expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        Frame.__init__(self, frame)

        self.windows_item = self.canvas.create_window(0, 0, window=self, anchor='nw')

    def __fill_canvas(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width=canvas_width)

    def update(self):
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))


class Simulator:
    def __init__(self, master):
        self.master = master
        master.title("Symulator")

        # frame
        self.main_frame = Frame(window, width=300, height=370, bg='grey')
        self.main_frame.pack(side='left', fill='both', padx=5, pady=5, expand=False)
        self.main_frame = Scrollable(self.main_frame, width=16)
        self.main_frame.config(bg='grey')

        self.xbh_frame = Frame(self.main_frame, width=300, height=185, bg='grey')
        self.xbh_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xba_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.xba_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.ss_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.ss_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xs_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.xs_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xp_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.xp_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xnd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.xnd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.snd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.snd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.snh_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.snh_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.sno_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.sno_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.so_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.so_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.time_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.time_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.params_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.params_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.kla_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.kla_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xsd_frame = Frame(self.main_frame, width=100, height=185, bg='grey')
        self.xsd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xpd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.xpd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.xndd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.xndd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.ssd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.ssd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.sndd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.sndd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.snhd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.snhd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.snod_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.snod_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.sod_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.sod_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.qd_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.qd_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.time_interval_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.time_interval_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

        self.buttons_frame = Frame(self.main_frame, width=90, height=185, bg='grey')
        self.buttons_frame.pack(side='left', fill='both', padx=5, pady=5, expand=False)

        Label(self.xbh_frame, text="Xbh", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.xba_frame, text="Xba", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.ss_frame, text="Ss", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.xs_frame, text="Xs", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.xp_frame, text="Xp", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.xnd_frame, text="Xnd", font="none 12 bold", width=4).pack(side='left', padx=5, pady=8)
        Label(self.snd_frame, text="Snd", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.snh_frame, text="Snh", font="none 12 bold", width=4).pack(side='left', padx=5, pady=8)
        Label(self.sno_frame, text="Sno", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.so_frame, text="So", font="none 12 bold", width=4).pack(side='left', padx=5, pady=7)
        Label(self.time_frame, text="krok", font="none 12 bold", width=4).pack(side='left', padx=5, pady=8)
        Label(self.kla_frame, text="kLa", font="none 12 bold", width=4).pack(side='left', padx=5, pady=8)
        Label(self.xsd_frame, text="Xs dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=8)
        Label(self.xpd_frame, text="Xp dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=8)
        Label(self.xndd_frame, text="Xnd dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=6)
        Label(self.ssd_frame, text="SS dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=6)
        Label(self.sndd_frame, text="Snd dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=8)
        Label(self.snhd_frame, text="Snh dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=8)
        Label(self.snod_frame, text="Sno dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=8)
        Label(self.sod_frame, text="So dopływ", font="none 12 bold", width=8).pack(side='left', padx=5, pady=8)
        Label(self.qd_frame, text="Natężenie przepływu", font="none 12 bold").pack(side='left', padx=5, pady=8)
        Label(self.time_interval_frame, text="Opóźnienie", font="none 12 bold").pack(side='left', padx=5, pady=8)

        # initself.entry_frame
        self.entry_value_xbh = DoubleVar(self.xbh_frame, value=reactor.Xbh)
        self.enter_xbh = Entry(self.xbh_frame, textvariable=self.entry_value_xbh, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_xba = DoubleVar(self.xba_frame, value=reactor.Xba)
        self.enter_xba = Entry(self.xba_frame, textvariable=self.entry_value_xba, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_ss = DoubleVar(self.ss_frame, value=reactor.Ss)
        self.enter_ss = Entry(self.ss_frame, textvariable=self.entry_value_ss, width=10).pack(side='left', padx=5,
                                                                                              pady=5)

        self.entry_value_xs = DoubleVar(self.xs_frame, value=reactor.Xs)
        self.enter_xs = Entry(self.xs_frame, textvariable=self.entry_value_xs, width=10).pack(side='left', padx=5,
                                                                                              pady=5)

        self.entry_value_xp = DoubleVar(self.xp_frame, value=reactor.Xp)
        self.enter_xp = Entry(self.xp_frame, textvariable=self.entry_value_xp, width=10).pack(side='left', padx=5,
                                                                                              pady=5)

        self.entry_value_xnd = DoubleVar(self.xnd_frame, value=reactor.Xnd)
        self.enter_xnd = Entry(self.xnd_frame, textvariable=self.entry_value_xnd, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_snd = DoubleVar(self.snd_frame, value=reactor.Snd)
        self.enter_snd = Entry(self.snd_frame, textvariable=self.entry_value_snd, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_snh = DoubleVar(self.snh_frame, value=reactor.Snh)
        self.enter_snh = Entry(self.snh_frame, textvariable=self.entry_value_snh, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_sno = DoubleVar(self.sno_frame, value=reactor.Sno)
        self.enter_sno = Entry(self.sno_frame, textvariable=self.entry_value_sno, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_so = DoubleVar(self.so_frame, value=reactor.So)
        self.enter_so = Entry(self.so_frame, textvariable=self.entry_value_so, width=10).pack(side='left', padx=5,
                                                                                              pady=5)

        # czas
        self.entry_value_time = DoubleVar(self.time_frame, value=reactor.t[-1])
        self.enter_time = Entry(self.time_frame, textvariable=self.entry_value_time, width=10).pack(side='left', padx=5,
                                                                                                    pady=5)

        Label(self.params_frame, text="Parametry dopływu", font="none 12 bold").pack(side='left', padx=5, pady=5)

        # doplyw
        self.entry_value_kla = DoubleVar(self.kla_frame, value=reactor.kla)
        self.enter_kla = Entry(self.kla_frame, textvariable=self.entry_value_kla, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_xsd = DoubleVar(self.xsd_frame, value=reactor.Xsd)
        self.enter_xsd = Entry(self.xsd_frame, textvariable=self.entry_value_xsd, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_xpd = DoubleVar(self.xpd_frame, value=reactor.Xpd)
        self.enter_xpd = Entry(self.xpd_frame, textvariable=self.entry_value_xpd, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_xndd = DoubleVar(self.xndd_frame, value=reactor.Xndd)
        self.enter_xndd = Entry(self.xndd_frame, textvariable=self.entry_value_xndd, width=10).pack(side='left', padx=5,
                                                                                                    pady=5)

        self.entry_value_ssd = DoubleVar(self.ssd_frame, value=reactor.Ssd)
        self.enter_ssd = Entry(self.ssd_frame, textvariable=self.entry_value_ssd, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_sndd = DoubleVar(self.sndd_frame, value=reactor.Sndd)
        self.enter_sndd = Entry(self.sndd_frame, textvariable=self.entry_value_sndd, width=10).pack(side='left', padx=5,
                                                                                                    pady=5)

        self.entry_value_snhd = DoubleVar(self.snhd_frame, value=reactor.Snhd)
        self.enter_snhd = Entry(self.snhd_frame, textvariable=self.entry_value_snhd, width=10).pack(side='left', padx=5,
                                                                                                    pady=5)

        self.entry_value_snod = DoubleVar(self.snod_frame, value=reactor.Snod)
        self.enter_snod = Entry(self.snod_frame, textvariable=self.entry_value_snod, width=10).pack(side='left', padx=5,
                                                                                                    pady=5)

        self.entry_value_sod = DoubleVar(self.sod_frame, value=reactor.Sod)
        self.enter_sod = Entry(self.sod_frame, textvariable=self.entry_value_sod, width=10).pack(side='left', padx=5,
                                                                                                 pady=5)

        self.entry_value_qd = DoubleVar(self.qd_frame, value=reactor.Qd)
        self.enter_qd = Entry(self.qd_frame, textvariable=self.entry_value_qd, width=8).pack(side='left', padx=5,
                                                                                             pady=5)

        self.entry_value_time_interval = DoubleVar(self.time_interval_frame, value=file_csv.czas)
        self.enter_value_time_interval = Entry(self.time_interval_frame, textvariable=self.entry_value_time_interval, width=8).pack(side='left', padx=5,
                                                                                             pady=5)

        # Labels

        # labels for values in real time
        self.show_xbh = Label(self.xbh_frame, textvariable=self.entry_value_xbh, font="none 12 bold")
        self.show_xbh.pack(side='left', padx=5, pady=7)

        self.show_xba = Label(self.xba_frame, textvariable=self.entry_value_xba, font="none 12 bold")
        self.show_xba.pack(side='left', padx=5, pady=7)

        self.show_ss = Label(self.ss_frame, textvariable=self.entry_value_ss, font="none 12 bold")
        self.show_ss.pack(side='left', padx=5, pady=7)

        self.show_xs = Label(self.xs_frame, textvariable=self.entry_value_xs, font="none 12 bold")
        self.show_xs.pack(side='left', padx=5, pady=7)

        self.show_xp = Label(self.xp_frame, textvariable=self.entry_value_xp, font="none 12 bold")
        self.show_xp.pack(side='left', padx=5, pady=7)

        self.show_xnd = Label(self.xnd_frame, textvariable=self.entry_value_xnd, font="none 12 bold")
        self.show_xnd.pack(side='left', padx=5, pady=8)

        self.show_snd = Label(self.snd_frame, textvariable=self.entry_value_snd, font="none 12 bold")
        self.show_snd.pack(side='left', padx=5, pady=7)

        self.show_snh = Label(self.snh_frame, textvariable=self.entry_value_snh, font="none 12 bold")
        self.show_snh.pack(side='left', padx=5, pady=8)

        self.show_sno = Label(self.sno_frame, textvariable=self.entry_value_sno, font="none 12 bold")
        self.show_sno.pack(side='left', padx=5, pady=7)

        self.show_so = Label(self.so_frame, textvariable=self.entry_value_so, font="none 12 bold")
        self.show_so.pack(side='left', padx=5, pady=7)
        # czas
        self.show_time = Label(self.time_frame, textvariable=self.entry_value_so, font="none 12 bold")
        self.show_time.pack(side='left', padx=5, pady=8)
        # doplyw

        self.show_kla = Label(self.kla_frame, textvariable=self.entry_value_kla, font="none 12 bold")
        self.show_kla.pack(side='left', padx=5, pady=7)

        self.show_xsd = Label(self.xsd_frame, textvariable=self.entry_value_xsd, font="none 12 bold")
        self.show_xsd.pack(side='left', padx=5, pady=7)

        self.show_xpd = Label(self.xpd_frame, textvariable=self.entry_value_xpd, font="none 12 bold")
        self.show_xpd.pack(side='left', padx=5, pady=7)

        self.show_xndd = Label(self.xndd_frame, textvariable=self.entry_value_xndd, font="none 12 bold")
        self.show_xndd.pack(side='left', padx=5, pady=7)

        self.show_ssd = Label(self.ssd_frame, textvariable=self.entry_value_ssd, font="none 12 bold")
        self.show_ssd.pack(side='left', padx=5, pady=7)

        self.show_sndd = Label(self.sndd_frame, textvariable=self.entry_value_sndd, font="none 12 bold")
        self.show_sndd.pack(side='left', padx=5, pady=8)

        self.show_snhd = Label(self.snhd_frame, textvariable=self.entry_value_snhd, font="none 12 bold")
        self.show_snhd.pack(side='left', padx=5, pady=7)

        self.show_snod = Label(self.snod_frame, textvariable=self.entry_value_snod, font="none 12 bold")
        self.show_snod.pack(side='left', padx=5, pady=7)

        self.show_sod = Label(self.sod_frame, textvariable=self.entry_value_sod, font="none 12 bold")
        self.show_sod.pack(side='left', padx=5, pady=7)

        self.show_qd = Label(self.qd_frame, textvariable=self.entry_value_qd, font="none 12 bold")
        self.show_qd.pack(side='left', padx=5, pady=8)

        self.show_time_interval = Label(self.time_interval_frame, textvariable=self.entry_value_time, font="none 12 bold")
        self.show_time_interval.pack(side='left', padx=5, pady=8)

        # Label(define, text='Symulator', bg="black", fg="white", font="none 12 bold").pack()

        # Buttons
        Button(self.buttons_frame, text="Rozpocznij symulacje", width="15",
               command=lambda: self.start_simulation()).pack(
            side='top', padx=5, pady=5)
        Button(self.buttons_frame, text="Wykres Reaktora", width="15", command=lambda: self.obrazek()).pack(side='top',
                                                                                                         padx=5,
                                                                                                         pady=5)
        Button(self.buttons_frame, text="Wyzeruj", width="15", command=lambda: self.wyzeruj()).pack(
            side='bottom', padx=5,
            pady=5)

        Button(self.buttons_frame, text="Zmień dopływ", width="15", command=lambda: self.inflow()).pack(
            side='top', padx=5,
            pady=5)

        Button(self.buttons_frame, text="Wykres osadnika", width="15", command=lambda: self.graph_settler()).pack(
            side='top', padx=5,
            pady=5)

        self.interval_time = file_csv.czas * 1000

    def start_simulation(self):
        if os.path.isfile("data.csv"):
            print("Najpierw zakoncz poprzednia symulacje")
        else:

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

            t = float(self.entry_value_time.get())
            file_csv.model.t[-1] = t
            file_csv.makesimulation.add_time = t
            file_csv.makesimulation.add_time1 = t

            kla1 = float(self.entry_value_kla.get())
            file_csv.model.kla = kla1

            xsd1 = float(self.entry_value_xsd.get())
            file_csv.model.Xsd = xsd1

            xpd1 = float(self.entry_value_xpd.get())
            file_csv.model.Xpd = xpd1

            xndd1 = float(self.entry_value_xndd.get())
            file_csv.model.Xndd = xndd1

            ssd1 = float(self.entry_value_ssd.get())
            file_csv.model.Ssd = ssd1

            sndd1 = float(self.entry_value_sndd.get())
            file_csv.model.Sndd = sndd1

            snhd1 = float(self.entry_value_snhd.get())
            file_csv.model.Snhd = snhd1

            snod1 = float(self.entry_value_snod.get())
            file_csv.model.Snod = snod1

            sod1 = float(self.entry_value_sod.get())
            file_csv.model.Sod = sod1

            qd1 = float(self.entry_value_qd.get())
            file_csv.model.Qd = qd1

            time_interval1 = float(self.entry_value_time_interval.get())
            file_csv.czas = time_interval1

            self.interval_time = file_csv.czas * 1000

            file_csv.only_for_close_function = True
            _thread.start_new_thread(file_csv.makesimulation, (t, t))

    def obrazek(self):
        if os.path.isfile("data.csv"):
            x = hasattr(self, 'figure1')
            if x:
                print("najpiew zakoncz symulacja")
            elif not x:
                x1 = hasattr(self, 'figure2')
                if x1:
                    for item in self.canvas.get_tk_widget().find_all():
                        self.canvas.get_tk_widget().delete(item)
                    del self.canvas
                    del self.figure2
                    self.graph_frame.destroy()

                    self.graph_frame = Frame(window, width=600, height=400, bg='grey')
                    self.graph_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)
                    self.x = Reactor.graphs
                    self.figure1 = plt.gcf()
                    self.canvas = FigureCanvasTkAgg(self.figure1, master=self.graph_frame)

                    self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
                    self.ani = FuncAnimation(plt.gcf(), self.x, interval=self.interval_time)
                    self.canvas.draw()

                elif not x1:
                    self.graph_frame = Frame(window, width=600, height=400, bg='grey')
                    self.graph_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)
                    self.x = Reactor.graphs
                    self.figure1 = plt.gcf()
                    self.canvas = FigureCanvasTkAgg(self.figure1, master=self.graph_frame)

                    self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
                    self.ani = FuncAnimation(plt.gcf(), self.x, interval=self.interval_time)
                    self.canvas.draw()
        else:
            print("najpierw rozpocznij symulacje")

    def _refit_artists(self):
        self.axis.relim()
        self.axis.autoscale_view()

    def update_plot(self, _):
        data = pd.read_csv('data.csv')

        self.z = np.array(
            [data['layer1'], data['layer2'], data['layer3'], data['layer4'], data['layer5'], data['layer6'],
             data['layer7'], data['layer8'], data['layer9'], data['layer10']])
        self.x = data['t']
        self.y = np.array([data['1'], data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'],
                           data['9'], data['10']])
        self.axis.clear()
        self.plot = self.axis.plot_surface(self.x, self.y, self.z)
        self.axis.set_xlabel('czas')
        self.axis.set_ylabel('warstwa')
        self.axis.set_zlabel('stężenie')

        self.line.recache_always()
        self._refit_artists()


    def graph_settler(self):
        if os.path.isfile("data.csv"):
            x = hasattr(self, 'figure2')
            if x:
                print("najpiew zakoncz symulacje")
            elif not x:
                x1 = hasattr(self, 'figure1')
                if x1:
                    for item in self.canvas.get_tk_widget().find_all():
                        self.canvas.get_tk_widget().delete(item)
                    del self.canvas
                    del self.figure1
                    self.graph_frame.destroy()

                    self.graph_frame = Frame(window, width=600, height=400, bg='grey')
                    self.graph_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)

                    self.figure2 = Figure((5, 5), 100)
                    self.canvas = FigureCanvasTkAgg(self.figure2, master=self.graph_frame)

                    self.canvas.draw()
                    toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame)
                    toolbar.update()
                    self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
                    # self.canvas.tkcanvas.pack()

                    self.axis = self.figure2.add_subplot(111, projection='3d')
                    self.x_data = np.array([0.1, 0.2, 0.3])
                    self.y_data = np.array([0.1, 0.2, 0.3])
                    self.z_data = np.array([[0.1], [0.2], [0.3]])
                    self.line = self.axis.plot([], [])[0]
                    self.line.set_data(self.x_data, self.y_data)

                    self.ani = FuncAnimation(self.figure2, self.update_plot, interval=self.interval_time)
                elif not x1:
                    self.graph_frame = Frame(window, width=600, height=400, bg='grey')
                    self.graph_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)

                    self.figure2 = Figure((5, 5), 100)
                    self.canvas = FigureCanvasTkAgg(self.figure2, master=self.graph_frame)

                    self.canvas.draw()
                    toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame)
                    toolbar.update()
                    self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
                    # self.canvas.tkcanvas.pack()

                    self.axis = self.figure2.add_subplot(111, projection='3d')
                    self.x_data = np.array([0.1, 0.2, 0.3])
                    self.y_data = np.array([0.1, 0.2, 0.3])
                    self.z_data = np.array([[0.1], [0.2], [0.3]])
                    self.line = self.axis.plot([], [])[0]
                    self.line.set_data(self.x_data, self.y_data)

                    self.ani = FuncAnimation(self.figure2, self.update_plot, interval=self.interval_time)



        else:
            print("najpierw rozpocznij symulacje")

    def wyzeruj(self):
        x1 = hasattr(self, 'canvas')
        x2 = hasattr(self, 'figure1')
        x3 = hasattr(self, 'figure2')
        if x1:
            for item in self.canvas.get_tk_widget().find_all():
                self.canvas.get_tk_widget().delete(item)
            del self.canvas
            self.graph_frame.destroy()
        elif not x1:
            print("Symulacja zostala juz zakonczona")

        if x2:
            del self.figure1
        if x3:
            plt.clf()
            plt.cla()
            plt.close()
            del self.figure2


        file_csv.only_for_close_function = False
        file_csv.model.t = [0.0, 0.1]
        file_csv.model.X1 = 0
        file_csv.model.X2 = 0
        file_csv.model.X3 = 0
        file_csv.model.X4 = 0
        file_csv.model.X5 = 0
        file_csv.model.X6 = 0
        file_csv.model.X7 = 0
        file_csv.model.X8 = 0
        file_csv.model.X9 = 0
        file_csv.model.X10 = 0

        if os.path.isfile("data.csv"):
            os.remove("data.csv")
        else:
            print("symulacja zostala juz zakonczona")

    def inflow(self):
        kla1 = float(self.entry_value_kla.get())
        file_csv.model.kla = kla1

        xsd1 = float(self.entry_value_xsd.get())
        file_csv.model.Xsd = xsd1

        xpd1 = float(self.entry_value_xpd.get())
        file_csv.model.Xpd = xpd1

        xndd1 = float(self.entry_value_xndd.get())
        file_csv.model.Xndd = xndd1

        ssd1 = float(self.entry_value_ssd.get())
        file_csv.model.Ssd = ssd1

        sndd1 = float(self.entry_value_sndd.get())
        file_csv.model.Sndd = sndd1

        snhd1 = float(self.entry_value_snhd.get())
        file_csv.model.Snhd = snhd1

        snod1 = float(self.entry_value_snod.get())
        file_csv.model.Snod = snod1

        sod1 = float(self.entry_value_sod.get())
        file_csv.model.Sod = sod1

        qd1 = float(self.entry_value_qd.get())
        file_csv.model.Qd = qd1

        interval_time_1 = float(self.entry_value_time_interval.get())
        file_csv.czas = interval_time_1


    def label(self):
        pocz0 = DoubleVar()
        pocz0.set(round(file_csv.model.Xbh, 10))
        self.show_xbh.config(textvariable=pocz0)

        pocz1 = DoubleVar()
        pocz1.set(round(file_csv.model.Xba, 10))
        self.show_xba.config(textvariable=pocz1)

        pocz2 = DoubleVar(value=file_csv.model.Ss)
        pocz2.set(round(file_csv.model.Ss, 10))
        self.show_ss.config(textvariable=pocz2)

        pocz3 = DoubleVar(value=file_csv.model.Xs)
        pocz3.set(round(file_csv.model.Xs, 10))
        self.show_xs.config(textvariable=pocz3)

        pocz4 = DoubleVar(value=file_csv.model.Xp)
        pocz4.set(round(file_csv.model.Xp, 10))
        self.show_xp.config(textvariable=pocz4)

        pocz5 = DoubleVar(value=file_csv.model.Xnd)
        pocz5.set(round(file_csv.model.Xnd, 10))
        self.show_xnd.config(textvariable=pocz5)

        pocz6 = DoubleVar(value=file_csv.model.Snd)
        pocz6.set(round(file_csv.model.Snd, 10))
        self.show_snd.config(textvariable=pocz6)

        pocz7 = DoubleVar(value=file_csv.model.Snh)
        pocz7.set(round(file_csv.model.Snh, 10))
        self.show_snh.config(textvariable=pocz7)

        pocz8 = DoubleVar(value=file_csv.model.Sno)
        pocz8.set(round(file_csv.model.Sno, 10))
        self.show_sno.config(textvariable=pocz8)

        pocz9 = DoubleVar(value=file_csv.model.So)
        pocz9.set(round(file_csv.model.So, 10))
        self.show_so.config(textvariable=pocz9)

        pocz_time = DoubleVar(value=file_csv.model.t[-1])
        pocz_time.set(round(file_csv.model.t[-1], 10))
        self.show_time.config(textvariable=pocz_time)

        pocz_kla = DoubleVar(value=file_csv.model.kla)
        pocz_kla.set(round(file_csv.model.kla, 10))
        self.show_kla.config(textvariable=pocz_kla)

        pocz_xsd = DoubleVar(value=file_csv.model.Xsd)
        pocz_xsd.set(round(file_csv.model.Xsd, 10))
        self.show_ssd.config(textvariable=pocz_xsd)

        pocz_xpd = DoubleVar(value=file_csv.model.Xpd)
        pocz_xpd.set(round(file_csv.model.Xpd, 10))
        self.show_xpd.config(textvariable=pocz_xpd)

        pocz_xndd = DoubleVar(value=file_csv.model.Xndd)
        pocz_xndd.set(round(file_csv.model.Xndd, 10))
        self.show_xndd.config(textvariable=pocz_xndd)

        pocz_ssd = DoubleVar(value=file_csv.model.Ssd)
        pocz_ssd.set(round(file_csv.model.Ssd, 10))
        self.show_ssd.config(textvariable=pocz_ssd)

        pocz_sndd = DoubleVar(value=file_csv.model.Sndd)
        pocz_sndd.set(round(file_csv.model.Sndd, 10))
        self.show_sndd.config(textvariable=pocz_sndd)

        pocz_snhd = DoubleVar(value=file_csv.model.Snhd)
        pocz_snhd.set(round(file_csv.model.Snhd, 10))
        self.show_snhd.config(textvariable=pocz_snhd)

        pocz_snod = DoubleVar(value=file_csv.model.Snod)
        pocz_snod.set(round(file_csv.model.Snod, 10))
        self.show_snod.config(textvariable=pocz_snod)

        pocz_sod = DoubleVar(value=file_csv.model.Sod)
        pocz_sod.set(round(file_csv.model.Sod, 10))
        self.show_sod.config(textvariable=pocz_sod)

        pocz_qd = DoubleVar(value=file_csv.model.Qd)
        pocz_qd.set(round(file_csv.model.Qd, 10))
        self.show_qd.config(textvariable=pocz_qd)

        pocz_int_time = DoubleVar(value=file_csv.czas)
        pocz_int_time.set(round(file_csv.czas, 10))
        self.show_time_interval.config(textvariable=pocz_int_time)

        window.after(1000, self.label)


window = Tk()
window.maxsize(1800, 1200)
window.minsize(400, 750)
window.configure(background="grey")
gui = Simulator(window)
gui.main_frame.update()
gui.label()
window.mainloop()
