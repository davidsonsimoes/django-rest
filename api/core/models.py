from django.db import models

class Channel(models.Model):
    FREQ_TYPES = (
        ('FM', 'Frequancia FM'),
        ('AM', 'Frequencia AM'),
    )
    nome = models.CharField(max_length=50)
    frequencia = models.CharField(max_length=10)
    faixa_freq = models.CharField(max_length=10, choices=FREQ_TYPES)

    def __str__(self):
        return self.nome

class Event(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Program(models.Model):
    DAYS = (
        ('DOM', 'Domingo'),
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
        ('SAB', 'Sábado'),
    )
    horarios = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    dia = models.CharField(max_length=10, choices=DAYS)

    def __str__(self):
        return self.dia