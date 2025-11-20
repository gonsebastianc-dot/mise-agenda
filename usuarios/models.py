from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('PRO', 'Profesional'),
        ('CLI', 'Cliente'),
    ]
    
    tipo_usuario = models.CharField(max_length=3, choices=TIPO_USUARIO, default='CLI')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_tipo_usuario_display()})"
