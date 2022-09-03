from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_domainonly_email


# Create your models here.
class Person(models.Model):
    phone_number = PhoneNumberField()
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    birth_date = models.DateField()
    address1 = models.CharField(max_length=35)
    address2 = models.CharField(max_length=35)
    city = models.CharField(max_length=20)
    county = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    email = models.EmailField(validators=[validate_domainonly_email])
    