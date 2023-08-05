from django.db import models
from perfil.models import Categoria, Conta

class Valores(models.Model):
    choice_tipo = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )
    
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Use on_delete=models.CASCADE
    descricao = models.TextField()
    data = models.DateField()
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)  # Use on_delete=models.CASCADE
    tipo = models.CharField(max_length=1, choices=choice_tipo)
    
    def _str_(self):
        return self.descricao

class Conta(models.Model):
    # Definição dos campos da conta

    def delete(self, *args, **kwargs):
        # Excluir registros relacionados na tabela Valores
        Valores.objects.filter(conta=self).delete()

        # Excluir a conta
        super().delete(*args, **kwargs)
