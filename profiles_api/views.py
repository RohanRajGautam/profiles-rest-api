from rest_framework.view import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  '''Test API view'''

  def get(self, request, format=None):
    """List of API VIEW """
    an_apiview = [
      'rohan',
      'rohit',
      'khem',
      'babita',
    ]

    return Response({'message':'Hello!', 'an_apiview':an_apiview})