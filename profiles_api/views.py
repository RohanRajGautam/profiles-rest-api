from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters

from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
  '''Test API view'''

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """List of API VIEW """
    an_apiview = [
      'rohan',
      'rohit',
      'khem',
      'babita',
    ]

    return Response({'message':'Hello!', 'an_apiview':an_apiview})

  def post(self, request):
    """Create a hello message with our name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}!'
      return Response({'message': message})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

  def put(self, request, pk=None):
    return Response({'method':'PUT'})

  def patch(self, request, pk=None):
    return Response({'method':'PATCH'})

  def delete(self, request, pk=None):
    return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):

  serializer_class = serializers.HelloSerializer

  def list(self, request):
    a_viewset = [
      'rohan',
      'rohit',
      'babita',
      'khem',
    ]
    return Response({'message':'Hello', 'a_viewset':a_viewset})

  def create(self, request):

    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello, {name}'
      return Response({'message':message})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

  def retrieve(self, request, pk=None):
    return Response({'http_method':'GET'})

  def update(self, request, pk=None):
    return Response({'http_method':'PUT'})

  def partial_update(self, request, pk=None):
    return Response({'http_method':'PATCH'})

  def destroy(self, request, pk=None):
    return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle creating and updating profile"""
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()

  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'email',)