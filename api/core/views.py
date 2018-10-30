from django.shortcuts import render
from rest_framework import viewsets
from .models import Channel, Event, Program
from .serializers import ChannelSerializer, EventSerializer, ProgramSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer