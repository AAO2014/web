from django.shortcuts import render

from django.http import HttpResponse 
def index(request, *args, **kwargs):
    return HttpResponse('index')
def login(request, *args, **kwargs):
    return HttpResponse('login')
def signup(request, *args, **kwargs):
    return HttpResponse('signup')
def question(request, *args, **kwargs):
    return HttpResponse('question')
def ask(request, *args, **kwargs):
    return HttpResponse('ask')
def popular(request, *args, **kwargs):
    return HttpResponse('popular')
def new(request, *args, **kwargs):
    return HttpResponse('new')