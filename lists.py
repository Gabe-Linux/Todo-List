import pickle
import os.path
from Tkinter import Frame, Entry, Button, Label, FLAT, N, LEFT, RIGHT, X, END

class List():
	def __init__(self, filename):

		# Set variables
		self.file = filename
		self.list = []

		# If file doesn't exit, create it.
		if (not os.path.isfile(self.file)):
			open(self.file, 'w')
		# If file does exit, load it.
		else:
			self.list = pickle.load(open(self.file, 'rb'))

	def add_item(self, text):

		# If the text is not blank, add it to the list
		if not(text == ''):
			self.list.append(text)

	def remove_item(self, text):

		# Remove the text from the list
		self.list.remove(text)

	def save_list(self):

		# Open the file and save the list
		f = open(self.file, 'w')
		pickle.dump(self.list, f)
		f.close()

	def load_list(self):

		# Open the file and retrieve the list
		f = open(self.file, 'rb')
		self.list = pickle.load(f)
		f.close()


class TkList(List):
	def __init__(self, file, tk):
		List.__init__(self, file)

		# Create the frame with list items
		self.frame = Frame(tk, padx = 0, pady = 10, bd = 0)
		self.frame.pack()

		# Create the field to input new list items
		self.input = Entry(tk, width = 32, bd = 1, insertborderwidth = 1, relief = FLAT)
		self.input.pack(anchor = N, pady = 4, side = LEFT, fill = X)
		self.input.focus_set()
		self.input.bind('<Return>', lambda l: self.add_item(self.input.get()))

		# Create an add button to the input field
		Button(tk, text = "+", relief = FLAT, command = lambda: self.add_item(self.input.get())).pack(anchor = N, side = RIGHT)

		# Update the list frame
		self.update()
		
	def add_item(self, text):
		List.add_item(self, text)

		# Clear input field
		self.input.delete(0, END)

		# Update the list frame
		self.update()

	def remove_item(self, text):
		List.remove_item(self, text)

		# Update the list frame
		self.update()

	def checkbox(self, text):

		# Return a button that will remove the list item
		return Button(self.frame, text = "-", relief = FLAT, command = lambda: self.remove_item(text))

	def update(self):

		# Remove previous list items
		for child in self.frame.winfo_children():
			child.destroy()

		# Draw each item in the list
		i = 0
		for item in self.list:
			self.checkbox(item).grid(row = i)
			Label(self.frame, text = item).grid(row = i, column = 1)
			i = i + 1

		# Save the list
		List.save_list(self)