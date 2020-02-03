# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)


class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

      @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(category_name=value)

class Image(models.Model):
    image_name = models.CharField(max_length =60)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'imgs/')

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    class Meta:
        ordering = ['image_name']          
