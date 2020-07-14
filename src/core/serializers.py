from rest_framework import serializers
from core.models import TestModel



class TestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields =  ('id', 'first_name', 'last_name')