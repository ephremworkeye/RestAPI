from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book

# Create your views here.

class BookList(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'book/home.html'
