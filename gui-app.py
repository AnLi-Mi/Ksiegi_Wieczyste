from tkinter import *

window = Tk()
window.title("Księgi Wieczyste")

input_command = Label (window, text = "Wpisz bazę numeru Księgi Wieczystej: ")
input_command.pack()

user_input = Entry (window)
user_input.pack()
user_input.get()

submit_button = Button (window, text = "Sprawdź numer kontrolny")
submit_button.pack()

window.mainloop()
