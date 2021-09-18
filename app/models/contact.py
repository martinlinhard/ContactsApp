import uuid
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = uuid.uuid4()

    def __str__(self):
        return "Name = {0}, Email = {1}, ID = {2}".format(self.name, self.email, self.id)

    def to_json(self):
        return {
                "name": self.name,
                "email": self.email
        }
