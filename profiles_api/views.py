from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):

        an_apiview = [
            'aosdfadsf',
            'oakdsttdsfasdf',
            'asdfejifhjjf',
        ]
        return Response({'message': 'Hello', 'an_api': an_apiview})
    