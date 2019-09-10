class Contacts:
    def __init__(self, email_id, name, numbers):
        self.email_id = email_id
        self.name = name
        self.numbers = numbers


class ContactsDTO:
    def __init__(self, search, offset, count):
        self.search = search
        self.offset = offset
        self.count = count