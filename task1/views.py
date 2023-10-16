from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
