from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Catalog, Book
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.
def show_catalogs(request):
    context = {'nodes': Catalog.objects.all()}
    return render(request, "books/catalogs.html", context)


def index(request):
    context = {'books': Book.objects.all()}
    return render(request, "books/list.html", context)


def detail(request, book_id):
    catalog_id= get_object_or_404(Book, pk=book_id).catalog_id
    nodes = Catalog.objects.get(pk=catalog_id).get_ancestors(include_self=True)
    context = {'book': get_object_or_404(Book, pk=book_id), 'nodes': nodes}
    return render(request, "books/detail.html", context)


def show_search_book_catalog(request,catalog_id):
    pass
