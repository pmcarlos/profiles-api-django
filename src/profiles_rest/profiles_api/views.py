from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.
class HelloApiView(APIView):
  """Test API View"""

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Return list of Api View features"""

    an_apiview = [
      'Uses http methods as functions get, post, patch, put, delete',
      'It is similar to a django view',
      'Gets the most control over logic',
      'Its mapped manually to urls'
    ]

    return Response({
      'message': 'Hello',
      'api': an_apiview
    })

  def post(self, request):
    """Create a Hello message with our name"""

    serializer = serializers.HelloSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('name')
      msg = 'Hello {0}'.format(name)

      return Response({
        'message': msg
      })
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    """Handles updating an object"""

    return Response({
      'method': 'PUT'
    })

  def patch(self, request, pk=None):
    """Handles updating some fields on an object"""

    return Response({
      'method': 'PATCH'
    })

  def delete(self, request, pk=None):
    """Delete an object"""

    return Response({
      'method': 'DELETE'
    })

class HelloViewSet(viewsets.ViewSet):
  """Test api viewset"""

  def list(self, request):
    """Return a hello message"""

    a_viewset =[
      'Uses action(list, create, delete, update, partial_update',
      'Automatically to urls using Routers',
      'Viewset provides mroe functionallity with less code'
    ]

    return Response({
      'message': 'Hello', 'a_viewset': a_viewset
    })