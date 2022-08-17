from rest_framework import serializers
from .models import Pizzeria


class PizzerraListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = ['id', 'logo_image', 'pizzeria_name', 'city', 'zip_code', 'absolute_url']


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id', 'pizzeria_name', 'street', 'city', 'state', 'zip_code', 'website', 'phone_number', 'description', 'logo_image', 'email', 'active'
            ]
