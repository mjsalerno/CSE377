from Tkinter import *

master = Tk()
inp = StringVar()


def far():
    # f = c*9/5.0 + 32
    inp.set(round((float(s.get())*(5.0/9.0) + 32.0), 2))


s = Scale(master, from_=0, to=100)
s.pack()

e = Entry(master, textvariable=inp)
e.pack()

e.focus_set()

f = Button(master, text="Fahrenheit", width=10, command=far)

f.pack()

mainloop()
