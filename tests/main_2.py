import turtle
from tkinter import *

tk=Tk()
tk.resizable(0,0)
tk.title('Wielokaty')
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
turtle=turtle.RawPen(canvas)
tk.mainloop()
