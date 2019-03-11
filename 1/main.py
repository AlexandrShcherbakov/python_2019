import tkinter


root = tkinter.Tk()
button = tkinter.Button(root, text="Button 1", command=root.quit)
button.grid()
root.mainloop()
root.destroy()
