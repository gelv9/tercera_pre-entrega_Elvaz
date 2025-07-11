from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(help_text="Duración en horas")
    profesor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nombre