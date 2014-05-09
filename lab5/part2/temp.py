#!/usr/bin/env python
from Tkinter import *

master = Tk()
inp = StringVar()


def cel():
    # c = (f - 32)*5/9.0
    inp.set(round((float(inp.get()) - 32.0)*(5.0/9.0)))


def far():
    # f = c*9/5.0 + 32
    inp.set(round((float(inp.get())*(5.0/9.0) + 32.0), 2))


e = Entry(master, textvariable=inp)
e.pack()

e.focus_set()


c = Button(master, text="Celsius", width=10, command=cel)
f = Button(master, text="Fahrenheit", width=10, command=far)

c.pack()
f.pack()

mainloop()
