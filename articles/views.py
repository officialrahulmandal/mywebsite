# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Album
from django.template import loader
def index(request):
    all_albums=Album.objects.all()
    return render(request,'articles/index.html',{'all_albums':all_albums,})


def detail(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except:
        raise Http404("Album does not exist")
    return render(request,'articles/detail.html',{'album':album})

# Create your views here.
