from concurrent.futures import thread
from tkinter import *
from tkinter import messagebox

from unittest.test import support

from test import reactor_ASM1
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import file_csv
import threading
import _thread
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import runpy
import time
import subprocess
import os


window = Tk()
window.title("Simulator")
window.configure(background="black")

def search():
    t = Tk()
    t.iconbitmap('icon.ico')
    b = Button(text='test', command=exit)
    b.grid(row=0)
    t.mainloop()


def costam():
    _thread.start_new_thread(file_csv.makesimulation, ())


def obrazek():
    model = reactor_ASM1()
    x = reactor_ASM1.graphs
    figure1 = plt.gcf()
    canvas = FigureCanvasTkAgg(figure1, master=window)
    canvas.get_tk_widget().grid(column=1, row=1)
    ani = FuncAnimation(plt.gcf(), x, interval=1000)
    canvas.show()


# def on_closing():
#     messagebox.askokcancel(title="hello", message="hello")
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         window.destroy()


Label(window, text='wykres', bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)
Button(window, text="obliczenia", width="15", command=lambda: costam()).grid(row=7, column=0, sticky=W)
Button(window, text="wykres", width="15", command=obrazek).grid(row=8, column=0, sticky=W)

# window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
