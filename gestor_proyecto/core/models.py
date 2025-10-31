from django.db import models
from django.contrib.auth.models import User

# ---------------------------
# Modelo Proyecto
# ---------------------------
class Proyecto(models.Model):
    ESTADOS = [
        ('en_curso', 'En curso'),
        ('en_revision', 'En revisión final'),
        ('finalizado', 'Finalizado'),
    ]

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='en_curso')
    finalizado = models.BooleanField(default=False)
    presupuesto_inicial = models.DecimalField(max_digits=12, decimal_places=2)
    presupuesto_actual = models.DecimalField(max_digits=12, decimal_places=2)
    creador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='proyectos_creados'
    )
    encargado = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='proyectos_asignados'
    )

    def __str__(self):
        return f"{self.nombre} - {self.estado}"


# ---------------------------
# Modelo Actividad
# ---------------------------
class Actividad(models.Model):
    actividad = models.CharField(max_length=255)
    fecha = models.DateField()
    modificacion = models.DateTimeField(auto_now=True)
    ingreso = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    egreso = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='actividades')

    def __str__(self):
        return f"{self.actividad} ({self.proyecto.nombre})"


# ---------------------------
# Modelo HistorialPresupuesto
# ---------------------------
class HistorialPresupuesto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='historial')
    fecha = models.DateField()
    presupuesto_actual = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Historial {self.proyecto.nombre} - {self.fecha}"

