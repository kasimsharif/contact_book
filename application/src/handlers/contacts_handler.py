import json

from flask import request, current_app as app

from application.src.common.base_resource import BaseResource
from application.src.common.exceptions.error_handler import ErrorHandler
from application.src.common.response_utils import ok_response
from application.src.controller.contacts_access import ContactsAccess


class ContactsHandler(BaseResource):
    def __init__(self):
        self.contact_access = ContactsAccess()


    @ErrorHandler("Credit User Get", app)
    def get(self):
        """
        Get request to access contact list
        :return:
        """
        request_data = request.args.to_dict()
        app.logger.info("Received Contact get request")
        app.logger.info(json.dumps(request_data))
        response = self.contact_access.search_contact(request_data)
        return ok_response(response)

    @ErrorHandler("Credit User Post", app)
    def post(self):
        """
        Post Request to create contacts
        :return:
        """
        app.logger.info("Received Contact post request")
        request_data = request.get_json(force=True)
        response = self.contact_access.create_new_contacts(request_data)
        return ok_response(response)

    @ErrorHandler("Credit User Put", app)
    def put(self, contact_id):
        app.logger.info("Received Contact put request")
        request_data = request.get_json(force=True)
        response = self.contact_access.edit_contacts(request_data, contact_id)
        return ok_response(response)

    @ErrorHandler("Credit User Delete", app)
    def delete(self, contact_id):
        app.logger.info("Received Contact delete request")
        request_data = request.get_json(force=True)
        response = self.contact_access.delete_contacts(contact_id)
        return ok_response(response)

