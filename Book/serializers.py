from django.db.models.base import Model
from rest_framework import serializers

class AuthorSerilizer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()


class BookSerializer(serializers.Serializer):
    author = AuthorSerilizer()
    title = serializers.CharField()
    slug = serializers.SlugField()
    description = serializers.CharField() 