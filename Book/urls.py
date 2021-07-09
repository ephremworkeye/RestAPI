from django.urls import path
from .views import BookList, Home
from . import api_views


urlpatterns = [
    # path('', BookList.as_view(), name='book_lsit'),
    # path('home', Home.as_view(), name='home'),
    # path('api', api_views.count_books),
    # path('all', api_views.all_books),
    path('api/allbooks', api_views.AllBooks.as_view(), name='all_books'), # from model serializer
]
