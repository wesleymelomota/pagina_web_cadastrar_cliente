from django.db import models
import time

# Create your models here.

sexo_choices = ( ('m', 'masculino'), ('f', 'feminino'))

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=sexo_choices)
    email = models.EmailField(blank=True, null=True)
    cell = models.IntegerField()

    def format_data(self):
        return self.data_nascimento.strftime('%d/%m/%y')
