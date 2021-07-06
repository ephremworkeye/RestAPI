from django.urls import path
from .views import BookList
from . import api_views


urlpatterns = [
    path('', BookList.as_view(), name='book_lsit'),
    path('api', api_views.count_books)
]
