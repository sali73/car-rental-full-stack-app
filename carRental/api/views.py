from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import CarSerializer, CarMiniSerializer
from .models import Car
from rest_framework.response import Response


def list(request, *args, **kwargs):
    cars = Car.objects.all()
    serializer = CarMiniSerializer(cars, many=True)
    return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
