from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from library.models import Kitob

from .serializers import KitobSerializer

class KitobAPIView(generics.ListAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer