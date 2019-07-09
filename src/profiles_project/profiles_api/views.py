from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

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
