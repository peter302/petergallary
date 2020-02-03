# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.
# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    return render(request, 'welcome.html', {"images": images, "locations": locations})
