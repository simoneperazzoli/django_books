from django.contrib import admin
from .models import Publisher, Book, Catalog
from django_mptt_admin.admin import DjangoMpttAdmin


class CatalogAdmin(DjangoMpttAdmin):
    pass


admin.site.register(Book)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Publisher)
