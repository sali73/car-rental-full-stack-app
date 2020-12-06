from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'make', 'color', 'year', 'photo', 'seat_capacity', 'rate', 'current_mileage', 'note']


class CarMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'photo', 'rate']
