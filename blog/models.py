from django.db import models

class Noticia (models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome  

class Categoria(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
    
class Corpo (models.Model):
    corpo = models.TextField()
    ordem = models.IntegerField()
    noticia = models.ForeignKey("Noticia", on_delete=models.CASCADE)

    def __str__(self):
        return self.corpo[:50]

class Imagem (models.Model):
    nome = models.TextField(null=True)
    ordem = models.IntegerField()
    noticia = models.ForeignKey("Noticia", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Imagens"

    def __str__(self):
        return self.nome

class Comentario (models.Model):
    corpo = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)
    noticia = models.ForeignKey("Noticia", on_delete=models.CASCADE)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.corpo

class Usuario (models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome

class Contato (models.Model):
    nome = models.CharField(max_length=30)
    assunto = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    mensagem = models.TextField()

    def __strf__(self):
        return self.nome


