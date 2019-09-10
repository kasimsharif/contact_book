from application.src.common.exceptions.custom_error import CustomError
from application.src.domain.contacts import Contacts, ContactsDTO


def validate_post_contact_data(data):
    email_id = data["emailId"]
    name = data["name"]
    numbers = data["numbers"]
    for number in numbers:
        if not number.isdigit():
            raise CustomError(400, "Mobile number should be digits")
        if len(number) != 10:
            raise CustomError(400, "Mobile number should be length 10 digits")
    return Contacts(email_id, name, numbers)


def validate_get_contact_params(data):
    search = data.get("search")
    offset = int(data.get("offset", 0))
    count = int(data.get("count", 10))
    return ContactsDTO(search, offset, count)
