from rest_framework import serializers
import rest_framework


# function serializers
# from django.http import response
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Book
# from .serializers import BookSerializer

# class serilizer
from rest_framework import generics
from .models import Book, Author
from .serializers import AuthorSerilizer, BookSerilizer


# @api_view()
# def count_books(request):
#     num_books = Book.objects.count()
#     return Response({'num_books':num_books})

# @api_view()
# def all_books(request):
#     books = Book.objects.all()
#     book_serializer = BookSerializer(books, many=True)
#     return Response(book_serializer.data)

class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class AllAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer
