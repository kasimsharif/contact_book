from application.src.common.exceptions.custom_error import CustomError
from application.src.controller.dto.response_json import get_contact_json
from application.src.controller.dto.validator import validate_post_contact_data, validate_get_contact_params
from application.src.dao.contacts_dao import create_contact, filter_contact_by_search, get_all_contacts, update_contact, \
    delete_contact


class ContactsAccess:
    def create_new_contacts(self, data):
        """
        Create New Contacts
        :param data: [emailId, name, numbers]
        :return:
        """
        contact = validate_post_contact_data(data)
        try:
            contact_obj = create_contact(contact.email_id, contact.name, contact.numbers)
        except:
            raise CustomError(422, "Duplicate Contact Entry with [" + contact.email_id + "]")
        return get_contact_json(contact_obj)

    def search_contact(self, search_param):
        """
        Search contact by name/emailId
        :param search_param: search param for name/emailId
        :return: list of contact matching
        """
        contact_dto = validate_get_contact_params(search_param)
        if contact_dto.search:
            contact_objs = filter_contact_by_search(contact_dto.search)
            contact_objs = contact_objs[contact_dto.offset:contact_dto.offset + contact_dto.count]
        else:
            contact_objs = get_all_contacts()
            contact_objs = contact_objs[contact_dto.offset:contact_dto.offset + contact_dto.count]
        return {"contacts": [get_contact_json(contact_obj) for contact_obj in contact_objs]}

    def edit_contacts(self, data, contact_id):
        """
        Edit Contact information
        :param data:
        :param contact_id:
        :return:
        """
        contact = validate_post_contact_data(data)

        try:
            contact_obj = update_contact(contact_id, contact.email_id, contact.name, contact.numbers)
        except:
            raise CustomError(400, "Contact not found")
        return get_contact_json(contact_obj)

    def delete_contacts(self, contact_id):
        try:
            delete_contact(contact_id)
        except:
            raise CustomError(400, "Contact not found")
        return {}
