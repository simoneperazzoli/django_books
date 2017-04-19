from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'catalogs', views.show_catalogs, name='catalogs'),
    url(r'^$', views.index, name='books'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='book_detail'),
    url(r'^catalog/(?P<catalog_id>[0-9]+)/$', views.show_search_book_catalog, name='search_catalog'),
]
