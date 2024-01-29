import datetime

from django.db import models
from django.utils import timezone

class Evento(models.Model):
	nome = models.CharField(max_length=256)
	solicitante = models.CharField(max_length=256)
	tempo = models.DateTimeField()
	lugar = models.CharField(max_length=16)
	descricao = models.CharField(max_length=256)
	status = models.CharField(max_length=16)