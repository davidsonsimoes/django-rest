from rest_framework import serializers
from .models import Channel, Event, Program

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'nome', 'frequencia', 'faixa_freq')

class EventSerializer(serializers.ModelSerializer):
    event = serializers.StringRelatedField(many=True)
    class Meta:
        model = Event
        fields = ('id', 'nome', 'descricao', 'event')

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'horarios', 'dia')