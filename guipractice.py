from tkinter import *

root = Tk()

test=Label(root, text="Test")
test.grid(row=0)
rest=Label(root, text="past rest")
test.grid(row=1)
entry=Entry(root)
entry.grid(row=0, column=1)
enter=Button(root, text="Enter")
enter.grid(row=0, column=2)


root.mainloop()
