from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Foro(models.Model): #Representa el foro en sí
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Categoria(models.Model): #Representa las diferentes categorías de temas del foro
    nombre = models.CharField(max_length=2550)
    def __str__(self):
        return self.nombre

class Tema(models.Model): #Representa un tema de discusión del foro
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Post(models.Model): #Representa una publicación dentro de un tema
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Comentario(models.Model): #Representa un comentario hecho en respuesta a un Post
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.contenido