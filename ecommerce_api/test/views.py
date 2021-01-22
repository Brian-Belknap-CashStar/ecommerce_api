from rest_framework import generics, status, permissions
from rest_framework.response import Response


class TestForContextHandler(generics.GenericAPIView):
    def get(self, request):
        return Response("Hello World", status=status.HTTP_200_OK)

