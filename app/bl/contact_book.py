import json
from json import JSONDecodeError
from models.contact import Contact

FILE_NAME = "contacts.json"

class ContactBook:
    def __init__(self):
        self.contacts = [Contact("Testname", "Testmail")]
        self.write_to_file()
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


