from rest_framework import serializers
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import PhoneNumber


class TestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields =  ('id', 'first_name', 'last_name')

class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = ('id', 'phone', 'contact','platforms')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id','name','website','email','fax', 'description', 'department', 'contact_type', 'phone_contact_set')


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = ('id','name','description','details')

        