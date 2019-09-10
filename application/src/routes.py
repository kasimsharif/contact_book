from application.src.handlers.contacts_handler import ContactsHandler


def setup_routes(api):
    api.add_resource(ContactsHandler, '/contacts/', '/contacts/<int:contact_id>/')
