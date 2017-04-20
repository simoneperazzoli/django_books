# import moneyed
# from djmoney.models.fields import MoneyField
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
import datetime
from django.utils.translation import ugettext as _
from versatileimagefield.fields import VersatileImageField
from .tasks import add as tadd

YEAR_CHOICES = [(r, r) for r in range(1960, datetime.date.today().year + 1)]


class Catalog(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    pages = models.PositiveSmallIntegerField()  # 32767
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, )
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE, )
    cover = VersatileImageField(
        'Image',
        upload_to='images/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        tadd.delay(10, 100)
        super(Book, self).save(*args, **kwargs)


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


        # <select id="year">
        # {% for y in range(1960, (datetime.datetime.now().year + 1)) %}
        #     <option value="{{ y }}">{{ y }}</option>./
        # {% endfor %}
        # </select>
