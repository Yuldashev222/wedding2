from django.shortcuts import render
from django.views.generic import ListView, View


def index(request):

    return render(request, 'index-5.html', {})