from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.serializers import TestModelSerializer
from core.serializers import ContactSerializer
from core.serializers import ScholarshipSerializer

# Create your views here.


# def test_view(request):
#     data = {'first_name': 'John', 'last_name': 'Brown'}
#     return JsonResponse(data)


class TestView(APIView):

    def get(self, request, format=None):
        test_models  = TestModel.objects.all()
        serializer  = TestModelSerializer(test_models, many=True)
        return Response(serializer.data)

class ContactView(APIView):

    def get(self, request, format=None):
        contact_models = Contact.objects.all()
        serializer = ContactSerializer(contact_models,many=True)
        return Response(serializer.data)
        
class ScholarshipView(APIView):

    def get(self, request, format=None):
        scholarship_models = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarship_models,many=True)
        return Response(serializer.data)
