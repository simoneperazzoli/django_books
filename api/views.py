from django_books.users.models import User
from books.models import Book
from rest_framework import viewsets
from api.serializers import UserSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-updated_at')
    serializer_class = BookSerializer
