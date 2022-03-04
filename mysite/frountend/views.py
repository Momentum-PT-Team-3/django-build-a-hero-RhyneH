from django.shortcuts import render
from django.core import serializers 
from django.http import JsonResponse
from .forms import HeroForm 
from myapi.models import Hero


def index(request):
    hero_form = HeroForm()
    return render(request, 'home.html', {'hero_form': HeroForm})


# Create your views here.
