from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PizzerraListSerializer, PizzeriaDetailSerializer
from .models import Pizzeria

class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzerraListSerializer

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

