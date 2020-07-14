from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import TestModel
from core.serializers import TestModelSerializer

# Create your views here.


# def test_view(request):
#     data = {'first_name': 'John', 'last_name': 'Brown'}
#     return JsonResponse(data)


class TestView(APIView):

    def get(self, request, format=None):
        test_models  = TestModel.objects.all()
        serializer  = TestModelSerializer(test_models, many=True)
        return Response(serializer.data)
        

