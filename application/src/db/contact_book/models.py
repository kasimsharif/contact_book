from django.db import models


class Contact(models.Model):
    email_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)


class MobileNumber(models.Model):
    number = models.CharField(max_length=32)
    contact = models.ForeignKey(Contact)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
