from django.db import models

class Noticia (models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    corpo = models.TextField()
    imagem = models.TextField(null=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome  

class Categoria(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
  

    