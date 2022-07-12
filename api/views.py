from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    # queryset is required, to get all objects from database
    queryset = Book.objects.all()

    # serialize_class is required
    serializer_class = BookSerializer