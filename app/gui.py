from tkinter import *
from tkinter import ttk
from bl.contact_book import ContactBook

class Gui():
    def __init__(self):
        self.contact_book = ContactBook()
        self.init()

    def init(self):
        self.root = Tk()
        self.root.title("Feet to Meters")
        
        # Root window
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Heading
        self.contacts_lb = ttk.Label(self.mainframe, text="Contact App")
        self.contacts_lb.grid(row=0, column = 0, columnspan = 3)
        
        # Label / Input for name
        self.name_lb = ttk.Label(self.mainframe, text="Name:")
        self.name_lb.grid(row=1, column=0)
        self.name_input = ttk.Entry(self.mainframe)
        self.name_input.grid(row=1, column=1)
        
        # Label / Input for email
        self.email_lb = ttk.Label(self.mainframe, text="Email:")
        self.email_lb.grid(row=2, column=0)
        self.email_input = ttk.Entry(self.mainframe)
        self.email_input.grid(row=2, column=1, columnspan=2)

        # Buttons for adding / saving data
        self.add_btn = ttk.Button(self.mainframe, text="Add", command=self.on_add_clicked)
        self.add_btn.grid(row = 1, column = 3)
        self.save_btn = ttk.Button(self.mainframe, text="Save", command=self.on_save_clicked)
        self.save_btn.grid(row = 2, column = 3)

        
        # create a list box
        self.contacts_list_box = Listbox(self.mainframe)
        self.contacts_list_box.grid(row=3, column=1, columnspan=3)

        # set previous items
        self.add_contacts_from_book()

        # Init menu
        self.m = Menu(self.mainframe, tearoff=0)
        self.m.add_command(label="Delete", command=self.on_delete)
        self.contacts_list_box.bind('<Button-3>', self.do_popup)

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass

    def do_popup(self, event):
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()

    def get_current_selection(self):
        return self.contacts_list_box.curselection()

    def add_contacts_from_book(self):
        self.contacts_list_box.delete(0, END)
        contacts = self.contact_book.get_contacts_list()
        for c in contacts:
            self.contacts_list_box.insert(END, c)
        pass

    def on_add_clicked(self):
        # read values from gui
        name = self.name_input.get()
        email = self.email_input.get()

        # update contact book + gui
        self.contact_book.add_contact(name, email, self.contacts_list_box)
        pass

    def on_save_clicked(self):
        self.contact_book.write_to_file()
        pass

    def on_delete(self):
        self.contact_book.remove_contacts(list(self.contacts_list_box.curselection()))
        self.add_contacts_from_book()
        pass
