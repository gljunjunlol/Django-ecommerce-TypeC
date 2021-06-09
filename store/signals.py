from django.db.models.signals import post_save
from . models import Customer
from django.contrib.auth.models import User

def createCustomer(sender, instance, **kwargs):
    """Create a Customer object each time a User is created ; and link it.
    If don't do this, user is created but wont add to Customers list"""
    Customer.objects.get_or_create(user=instance)

post_save.connect(createCustomer, sender=User)