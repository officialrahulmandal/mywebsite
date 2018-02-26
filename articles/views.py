# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>hello welcome to article section")
def detail(request,album_id):
    return HttpResponse("<h2> Deatils for album id :-"+str(album_id)+"</h2>")

# Create your views here.
