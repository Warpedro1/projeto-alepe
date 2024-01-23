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

	def __init__(self, nome, solicitante, tempo, lugar, descricao, status):
		self.nome = nome
		self.solicitante = solicitante
		self.tempo = tempo
		self.lugar = lugar
		self.descricao = descricao
		self.status = status