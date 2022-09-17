from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length= 100)
    dt_criacao = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome
    

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null = True, blank= True)
    data = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.titulo

