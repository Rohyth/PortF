from django.shortcuts import render
# from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import HeroSerializers
from .models import Hero


def scrapper1(request):
    return render(request, 'Scrapper1.html')


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers


