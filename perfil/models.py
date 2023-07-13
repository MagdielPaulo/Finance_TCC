from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False) 
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria  
    
class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa econômica'),
    )