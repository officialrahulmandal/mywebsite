# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album
from django.template import loader
def index(request):
    all_albums=Album.objects.all()
    return render(request,'articles/index.html',{'all_albums':all_albums,})


def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'articles/detail.html',{'album':album})

# Create your views here.
