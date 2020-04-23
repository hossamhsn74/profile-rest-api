from django.shortcuts import render
from rest_framework import filters, permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from profiles_api import models, permissions, serializers


class HelloApiView(APIView):

    serializer_class = serializers.HelloApiSerializer

    def get(self, request, format=None):
        an_apiview = [
            'one',
            'two',
            'three'
        ]
        return Response({'message': 'this is a response', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'hello ' + name
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloApiSerializer

    """ returns a hello message """

    def list(self, request):
        a_viewset = [
            'test1',
            'test2',
        ]
        return Response({'message': 'this is viewset', 'data': a_viewset})

    """ create new hello message """

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'hello ' + name
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retreive(self, requeset, pk=None):
        """ handle getting data by ID """
        return Response({"http_method": 'GET'})

    def update(self, requeset, pk=None):
        """ handle updatung data  """
        return Response({"http_method": 'PUT'})

    def pertial_update(self, requeset, pk=None):
        """ handle pratcial data update """
        return Response({"http_method": 'PATCH'})

    def destroy(self, requeset, pk=None):
        """ handle removing an object """
        return Response({"http_method": 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and updating profiles """
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

    # permission wise variables
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.UpdateOwnProfile]

    # filteration and search function
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class UserLoginApiView(ObtainAuthToken):
    """  handle creating user authotication tokens   """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    queryset = models.ProfileFeedItem.objects.all()
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated, permissions.UpdateOwnStatus]

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
