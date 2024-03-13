from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def root(req):
    return HttpResponse('home page')

def rooms(req):
    return HttpResponse('rooms')
