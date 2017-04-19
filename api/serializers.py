from django_books.users.models import User
from books.models import Book
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ([f.name for f in Book._meta.get_fields()])


