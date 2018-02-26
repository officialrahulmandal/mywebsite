# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader
def index(request):
    all_albums=Album.objects.all()
    return render(request,'articles/index.html',{'all_albums':all_albums,})


def detail(request,album_id):
    return HttpResponse("<h2> Deatils for album id :-"+str(album_id)+"</h2>")

# Create your views here.
