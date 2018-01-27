from Tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
L2 = Label(top, text="And Password")
L2.pack( side = LEFT)
E2 = Entry(top, bd =5)
E2.pack(side = RIGHT)

top.mainloop()