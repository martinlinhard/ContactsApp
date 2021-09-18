import json
from json import JSONDecodeError
from models.contact import Contact
from tkinter import END

FILE_NAME = "contacts.json"

class ContactBook:
    def __init__(self):
        self.load_data()
        pass

    def load_data(self):
        try:
            with open(FILE_NAME) as f:
                data = json.load(f)
                self.contacts = []
                for item in data:
                    self.contacts.append(Contact(**item))
        except (FileNotFoundError, JSONDecodeError):
            print("Warning - No contacts.json was found in the current directory / The format was invalid --> Falling back to default config...")
            self.default_config()

    def default_config(self):
        self.contacts = []
        self.write_to_file()

    def write_to_file(self):
        contacts = list(map(lambda x: x.to_json(), self.contacts))

        with open (FILE_NAME, 'w') as f:
            json.dump(contacts, f)

    def add_contact(self, name, email, listbox):
        # update own content
        c = Contact(name, email)
        self.contacts.append(c)

        # update gui
        listbox.insert(END, c.for_gui())

    def get_contacts_list(self):
        return list(map(lambda c : c.for_gui(), self.contacts))

    def remove_contacts(self, indices):
        # remove all contacts
        contacts = list(map(lambda i: self.contacts[i], indices))
        for c in contacts:
            self.contacts.remove(c)
