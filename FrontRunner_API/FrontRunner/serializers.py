from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'birth_date', 'address1', 'address2', 'city', 'county', 'state', 'zip_code', 'email']