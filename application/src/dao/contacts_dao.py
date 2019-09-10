from django.db.models.query_utils import Q

from application.src.db.contact_book.models import Contact, MobileNumber


def create_contact(email_id, name, numbers):
    contact = Contact.objects.create(email_id=email_id, name=name)
    for number in numbers:
        MobileNumber.objects.create(number=number, contact=contact)

    return contact


def update_contact(contact_id, email_id, name, numbers):
    contact = Contact.objects.get(id=contact_id)
    contact.email_id = email_id
    contact.name = name
    contact.save()
    MobileNumber.objects.filter(contact=contact).delete()
    for number in numbers:
        MobileNumber.objects.create(number=number, contact=contact)

    return contact


def filter_mobile_number(**params):
    return MobileNumber.objects.filter(**params)


def filter_contact_by_search(search):
    return Contact.objects.filter(Q(email_id__icontains=search) | Q(name__icontains=search))


def get_all_contacts():
    return Contact.objects.all()

def delete_contact(contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
