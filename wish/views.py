from django.shortcuts import render
from .models import Wish
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework import filters

from .serializers import WishSerializer

# Create your views here.

class WishListView(generics.ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer

# class WishDetailView(APIView):

#     def get_object(self, id):
#         try:
#             return Wish.objects.get(pk=id)
#         except Wish.ObjectDoesNotExist: 
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, id):
#         wish = self.get_object(id)
#         serializer = WishSerializer(wish)
#         return Response(serializer.data)

#     def put(self, request, id):
#         wish = self.get_object(id)
#         serializer = WishSerializer(wish, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         wish = self.get_object(id)
#         wish.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class WishDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer

class WishSearchView(generics.ListCreateAPIView):
    search_fields = ['author', 'title']
    filter_backends = (filters.SearchFilter,)
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
