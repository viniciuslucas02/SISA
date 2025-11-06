from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    faculdade = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    turno = models.CharField(max_length=20)
    emitido = models.DateField()

