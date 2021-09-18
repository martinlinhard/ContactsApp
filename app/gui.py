from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

contacts_lb = ttk.Label(mainframe, text="Contact App")
contacts_lb.grid(row=0, column = 0, columnspan = 3)

name_lb = ttk.Label(mainframe, text="Name:")
name_lb.grid(row=1, column=0)
name_input = ttk.Entry(mainframe)
name_input.grid(row=1, column=1, columnspan=2)

email_lb = ttk.Label(mainframe, text="Email:")
email_lb.grid(row=2, column=0)
email_input = ttk.Entry(mainframe)
email_input.grid(row=2, column=1, columnspan=2)

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = StringVar(value=langs)

contacts_list_box = Listbox(mainframe, listvariable=langs_var)
contacts_list_box.grid(row=3, column=1, columnspan=3)

root.mainloop()
