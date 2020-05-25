from django.shortcuts import render
from .models import Wish
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .serializers import WishSerializer

# Create your views here.

class WishAPIView(APIView):

    def get(self, request):
        wishes = Wish.objects.all()
        serializer = WishSerializer(wishes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WishSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WishDetails(APIView):

    def get_object(self, id):
        try:
            return Wish.objects.get(pk=id)
        except ObjectDoesNotExist: 
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        wish = self.get_object(id)
        serializer = WishSerializer(wish)
        return Response(serializer.data)

    def put(self, request, id):
        wish = self.get_object(id)
        serializer = WishSerializer(wish, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        wish = self.get_object(id)
        wish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

