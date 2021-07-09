from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Author, Book

# Create your views here.

class BookList(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'book/home.html'


class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['books'] = Book.objects.all()
        context['authors'] = Author.objects.all()
        return context

       


