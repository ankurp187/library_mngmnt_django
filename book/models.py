from __future__ import unicode_literals

from datetime import datetime

from django.utils import timezone
from django.db import models
from django.contrib import admin

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    publish_date = models.DateField(default=timezone.now)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=10)

    def __str__(self):
        return str(self.id) + '. ' + self.name+' written by '+self.author


class Assignment(models.Model):
    roll_id = models.CharField(max_length=20)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(default=timezone.now)
    submitted_on = models.DateTimeField(default=timezone.make_aware(datetime.strptime('9999-12-31 23:59:59','%Y-%m-%d %H:%M:%S')))
    is_active = models.CharField(max_length=1,default='Y')



