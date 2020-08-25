from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import PhoneNumber
from core.models import NewsFeed
from core.models import Position
from core.models import GeometryObject
from core.models import GeoJSONFeature
from core.serializers import PhoneNumberSerializer
from django.db.models import Q
from core.models import Event
from core.serializers import TestModelSerializer
from core.serializers import ContactSerializer
from core.serializers import ScholarshipSerializer
from core.serializers import EventSerializer
from core.serializers import NewsFeedSerializer
from core.serializers import GeoJSONFeatureSerializer
from core.serializers import PositionSerializer
from core.serializers import GeometryObjectSerializer

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

    def get(self, request):
        qs = Contact.objects.all()

        dep = self.request.query_params.get('department')
        c_type = self.request.query_params.get('type')
        search = self.request.query_params.get('search')

        if dep in ['CHEM','COMP', 'GEO', 'LIFE', 'MATH', 'PHYS']:
            qs = qs.filter(department__exact=dep)
        
        if dep == 'OTHER':
            qs = qs.filter(Q(department__exact=dep) , ~Q(contact_type__exact='EMERGENCY') & ~Q(contact_type__exact='OTHER'))
        
        if c_type in ['EMERGENCY','OTHER']:
            qs = qs.filter(contact_type__exact=c_type)
        
        if search is not None and search != '':
            if len(search.split(' ')) ==1:
                qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(phone_contact_set__phone__icontains=search))
            else:
                search_list = search.split(' ')
                qs = qs.filter(*[Q(name__icontains=word) | Q(description__icontains=word) | Q(phone_contact_set__phone__icontains=word) for word in search_list])

        qs = qs.distinct()
        qs = qs.order_by('name')
        serializer = ContactSerializer(qs, many=True)
        
        return Response(serializer.data)

class PhoneNumberView(APIView):

    def get(self, request, format=None):
        phone_num_models = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(phone_num_models,many=True)
        return Response(serializer.data)

class ScholarshipView(APIView):

    def get(self, request, format=None):
        scholarship_models = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarship_models,many=True)
        return Response(serializer.data)

class EventView(APIView):

    def get(self, request, format = None):
        event_models = Event.objects.all()
        serializer = EventSerializer(event_models, many = True)
        return Response(serializer.data)

class NewsFeedView(APIView):

    def get(self, request, format=None):
        newsfeed_models = NewsFeed.objects.all()
        serializer = NewsFeedSerializer(newsfeed_models,many=True)
        return Response(serializer.data)


class GeoJSONFeatureView(APIView):
    def get(self, request, format=None):
        feature_models = GeoJSONFeature.objects.all()
        serializer = GeoJSONFeatureSerializer(feature_models,many=True)
        return Response(serializer.data)

class GeometryObjectView(APIView):
    def get(self, request, format=None):
        geometry_object_models = GeometryObject.objects.all()
        serializer = GeometryObjectSerializer(geometry_object_models,many=True)
        return Response(serializer.data)

class PositionView(APIView):
    def get(self, request, format=None):
        position_models = Position.objects.all()
        serializer = PositionSerializer(position_models,many=True)
        return Response(serializer.data)