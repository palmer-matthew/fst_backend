from rest_framework import serializers
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import Event


class TestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields =  ('id', 'first_name', 'last_name')

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id','name','website','email','fax','phone')

class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = ('id','name','description','details')

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date', 'start_time', 'end_date', 'end_time', 'location')

        