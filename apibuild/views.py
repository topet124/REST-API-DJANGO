from django.shortcuts import render
from rest_framework import viewsets
from .models import course
from .serializers import courseserializer

# Create your views here.
class courseview(viewsets.ModelViewSet):
       queryset= course.objects.all()
       serializer_class = courseserializer
    
