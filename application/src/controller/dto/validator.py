from application.src.common.exceptions.custom_error import CustomError
from application.src.domain.contacts import Contacts, ContactsDTO
import re

# Make a regular expression
# for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


# Define a function for
# for validating an Email
def check(email):
    # pass the regualar expression
    # and the string in search() method
    if not (re.search(regex, email)):
        raise CustomError(400, "Invalid Email Id")


def validate_post_contact_data(data):
    email_id = data["emailId"]
    check(email_id)
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
