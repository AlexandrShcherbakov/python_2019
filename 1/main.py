import tkinter


root = tkinter.Tk()
button = tkinter.Button(root, text="Button 1", command=root.quit)

increase_button = tkinter.Button(root, text="0")
def inc_func(*args):
	increase_button["text"] = str(int(increase_button["text"]) + 1)
increase_button.bind("<Button-1>", inc_func)

button.grid()
increase_button.grid()

root.mainloop()
root.destroy()
