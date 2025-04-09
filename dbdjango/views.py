from django.contrib import admin
from django.shortcuts import HttpResponse,render, redirect
from django.urls import path

def index(request):
    return HttpResponse('go')