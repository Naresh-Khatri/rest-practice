from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            'aosdfadsf',
            'oakdsttdsfasdf',
            'asdfejifhjjf',
        ]
        return Response({'message': 'Hello', 'an_api': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request, pk=None):
        return Response({'method': "PUT"})

    def patch(self,request, pk=None):
        return Response({'method': "PATCH"})

    def delete(self,request, pk=None):
        return Response({'method': "DELETE"})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        a_viewset=[
        'usefasfjasdlf',
        'adsfohefhbbhfhfhdsfsd',
        'jirhjjggurtj sfjosies fsd fosaijfo asdf as dfas df Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        ]
        return Response({'message':'hello', 'a_viewset': a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retriev(self, request, pk=None):
        return Response({'HTTP method': 'PUT'})

    def update(self, request, pk=None):
        return Response({'HTTP method': 'update'})

    def partial_update(self, request, pk=None):
        return Response({'HTTP method': 'partial_update'})

    def destroy(self, request, pk=None):
        return Response({'HTTP method': 'delete'})
