from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    
    STATUS_CHOICES = [
        ('Em Uso', 'Em Uso'),
        ('Estoque', 'Estoque'),
        ('Manutenção', 'Manutenção'),
    ]

    nome = models.CharField(max_length=150)
    serial = models.CharField(max_length=100, unique=True)
    data_aquisicao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Estoque')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.serial})"
