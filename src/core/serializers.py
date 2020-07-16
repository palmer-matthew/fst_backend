from rest_framework import serializers
from core.models import TestModel
from core.models import Contact


class TestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields =  ('id', 'first_name', 'last_name')

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id','name','website','email','fax','phone')