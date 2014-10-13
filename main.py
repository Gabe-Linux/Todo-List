from Tkinter import Tk
import lists

# Create a Tkinter window and set basic attributes
root = Tk()
root.geometry('300x450')
root.resizable(0, 0)
root.title("Todo List")

# Create a list using default.list
lists.TkList('default.list', root)

root.mainloop()