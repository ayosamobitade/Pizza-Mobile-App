from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PizzerraListSerializer
from .models import Pizzeria

class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzerraListSerializer


