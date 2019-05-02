from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

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

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses action(list, create, delete, update, partial_update',
            'Automatically to urls using Routers',
            'Viewset provides mroe functionallity with less code'
        ]

        return Response({
            'message': 'Hello', 'a_viewset': a_viewset
        })

    def create(self, request):
        """Create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if(serializer.is_valid()):
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)

            return Response({'message': message})

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Updated an specific object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Updates some parts of specific object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removin an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Check email and password an return an Auth Token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken api to validate and create a token"""

        return ObtainAuthToken().post(request)
