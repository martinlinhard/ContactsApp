from bl.contact_book import ContactBook

class Cli():
    def __init__(self):
        self.contact_book = ContactBook()

        self.handlers = {
            "a": self.handle_print,
            "b": self.handle_add,
            "c": self.handle_remove_contacts,
            "d": self.save_contacts,
            "e": self.handle_exit
        }

        self.options = {
                "a": "View all contacts",
                "b": "Add a new contact",
                "c": "Remove contact(s)",
                "d": "Save contacts",
                "e": "Exit application"
        }

    def run(self):
        print("Welcome to the Contact Book!")
        self.print_menu()
        pass

    # This method prints the menu and returns the option choosen
    # In case an invalid option is entered, the user is again prompted for a choice.
    def print_menu(self):
        print("\nPlease choose one of the options below:")

        for (key, value) in self.options.items():
            print('{0} ) {1}'.format(key, value))
        
        choice = input('Your choice: ')

        if choice not in self.handlers:
            self.print_menu()

        result = self.handlers[choice]()

        if result:
            self.print_menu()

        pass

    def handle_print(self):
        print('\nYour contacts:')
        for index, item in enumerate(self.contact_book.get_contacts_list()):
            print("{}. {}".format(index, item))
        return True

    def handle_add(self):
        print('\nAdd a new contact:')
        name = input("Name: ")
        email = input("Email: ")
        self.contact_book.add_contact(name, email)
        print("--> Contact {} ({}) has been added successfully.".format(name, email))
        return True

    def handle_remove_contacts(self):
        print('\nRemove contacts:')
        choices = input("Enter indices to be removed: ")
        indices = list(map(lambda x: int(x), choices.split(", ")))

        if any(map(lambda x: x > len(self.contact_book.contacts) - 1, indices)):
            print("Invalid index detected - Aborting...")
            return True

        self.contact_book.remove_contacts(indices)

        return True

    def save_contacts(self):
        self.contact_book.write_to_file()
        print("All contacts have been saved successfully!")
        return True

    def handle_exit(self):
        return False
