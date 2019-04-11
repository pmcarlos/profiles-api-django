from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
  """Test API View"""

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
