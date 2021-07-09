from django.db.models.base import Model
from rest_framework import serializers
from .models import Book, Author

# class AuthorSerilizer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     username = serializers.CharField()


# class BookSerializer(serializers.Serializer):
#     author = AuthorSerilizer()
#     title = serializers.CharField()
#     slug = serializers.SlugField()
#     description = serializers.CharField() 

# class based serializers
class AuthorSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'username']

class BookSerilizer(serializers.ModelSerializer):
    author = AuthorSerilizer()
    class Meta:
        model = Book
        fields = ['title', 'slug', 'author']