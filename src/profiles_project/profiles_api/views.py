from django.shortcuts import render

# viewsets is the base module for all views in django
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    # tell django the serializer to use to describe data to handle with api view
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patchm put, delete)',
            'It is similar to a traditional Django views',
            'gives you the most control over your logic',
            'is mapped manually to URLs'
        ]

        # response object must be passed a dictionary
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    # post request
    def post(self, request):
        """Create a hello message with our name"""

        # creates a serializer obj and passes in the request data to the data attr
        serializer = serializers.HelloSerializer(data=request.data)

        # check the serializer has valid data
        if serializer.is_valid():
            name = serializer.data.get('name')  # getting the name property
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk is primary key, put() identifies a particular object with the pk and updates it.
    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method': 'put'})

    # partially updating objects
    def patch(self, request, pk=None):
        """Pach request, only updates fields in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    # viewsets use different actions you would perform on an object
    def list(self, request):
        """Return a hello message"""

        # list the diff attrs of a viewset
        a_viewset = [
            'Uses actions (list, create, retrieve, partial_update)',
            'automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})
