from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Proyecto, Actividad, HistorialPresupuesto

# ---------------------------
# Extender UserAdmin para ver campos básicos
# ---------------------------
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Re-registrar User con el admin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# ---------------------------
# Admin Proyecto
# ---------------------------
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombre', 'estado', 'finalizado', 
        'presupuesto_inicial', 'presupuesto_actual', 
        'creador', 'encargado'
    )
    list_filter = ('estado', 'finalizado')
    search_fields = ('nombre', 'descripcion')
    raw_id_fields = ('creador', 'encargado')  # más fácil seleccionar usuarios
    ordering = ('fecha_creacion',)

# ---------------------------
# Admin Actividad
# ---------------------------
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'actividad', 'fecha', 'ingreso', 'egreso', 'proyecto', 'modificacion')
    list_filter = ('fecha', 'proyecto')
    search_fields = ('actividad', 'proyecto__nombre')
    raw_id_fields = ('proyecto',)
    ordering = ('fecha',)

# ---------------------------
# Admin HistorialPresupuesto
# ---------------------------
@admin.register(HistorialPresupuesto)
class HistorialPresupuestoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proyecto', 'fecha', 'presupuesto_actual')
    list_filter = ('fecha', 'proyecto')
    search_fields = ('proyecto__nombre',)
    raw_id_fields = ('proyecto',)
    ordering = ('-fecha',)
