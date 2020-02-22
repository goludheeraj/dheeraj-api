from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Recturn a list of APIview features"""
        an_apiview = [

            'Uses HTTP method as function (get, post, batch, put, delete)',
            'IS similar to a traditional Django view',
            'Gives you the most control over you application logic',
            'IS mapped manually to URLs',

            ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})
