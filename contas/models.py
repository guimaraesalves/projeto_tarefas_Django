from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    objects = None
    data = models.DateTimeField()
    #nome = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao
