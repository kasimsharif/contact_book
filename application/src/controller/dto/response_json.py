from application.src.dao.contacts_dao import filter_mobile_number


def get_contact_json(contact_obj):
    mobile_list = []
    mobile_obj = filter_mobile_number(contact=contact_obj)
    for each_obj in mobile_obj:
        mobile_list.append(each_obj.number)
    return {
        "id": contact_obj.id,
        "emailId": contact_obj.email_id,
        "name": contact_obj.name,
        "numbers": mobile_list
    }
