import datetime

from django.db import models
from django.utils import timezone

OPCOES_STATUS = [
	("AGENDADO", "Agendado"),
	("EM PROGRESSO", "Em Progresso"),
	("CONCLUIDO", "Concluido"),
]

class Evento(models.Model):
	nome = models.CharField(max_length=256, null=False, blank=False)
	solicitante = models.CharField(max_length=256, null=False, blank=False)
	tempo = models.DateTimeField(null=False, blank=False)
	lugar = models.CharField(max_length=16, null=False, blank=False)
	descricao = models.CharField(max_length=256, null=False, blank=False)
	status = models.CharField(max_length=16, choices=OPCOES_STATUS, default='', null=False, blank=False)

	def __str__(self):
		return f"Nome: {self.nome}, Solicitante: {self.solicitante}, Tempo: {self.tempo}, Lugar: {self.lugar}, Descrição: {self.descricao}, Status: {self.status}"