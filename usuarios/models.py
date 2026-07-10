from django.db import models

# Create your models here.
class Cliente(models.Model):
    QUEIXA_CHOICES = {
        ('A', 'Ansiedade'),
        ('D', 'Depressão'),
    }
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    queixa = models.CharField(max_length=1, choices=QUEIXA_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nome