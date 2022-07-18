from rest_framework import serializers
from .models import Pizzeria


class PizzerraListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = ['id', 'logo_image', 'pizzeria_name', 'city', 'zip_code', 'absolute_url']