import uuid
class Contact:
    def __init__(self, name, email, id=uuid.uuid4()):
        self.name = name
        self.email = email
        self.id = id

    def __str__(self):
        return "Name = {0}, Email = {1}, ID = {2}".format(self.name, self.email, self.id)

    def to_json(self):
        return {
                "name": self.name,
                "email": self.email,
                "id": self.id.__str__()
        }

    def for_gui(self):
        return "{0} - {1}".format(self.name, self.email)
