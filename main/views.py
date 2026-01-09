from django.shortcuts import render


from .serializers import NoteSerializer
from .models import Note
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

