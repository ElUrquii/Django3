from django.contrib import admin
from .models import *

# register your models here.

class MaterialAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class PersonaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class AlumnoInline(admin.TabularInline):
    model = Alumno

class ProfesorInline(admin.TabularInline):
    model = Profesor

class LibroInline(admin.TabularInline):
    model = Libro

class RevistaInline(admin.TabularInline):
    model = Revista

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('codigo','fechaSalida', 'fechaRegreso')
    list_display_links = ('codigo','fechaSalida', 'fechaRegreso')
    search_fields = ('codigo','fechaSalida', 'fechaRegreso')
    inlines = [AlumnoInline, ProfesorInline, LibroInline, RevistaInline]

class LibroAdmin(admin.ModelAdmin):
    list_display = ('tipoMaterial','autor','titulo','anio','status','prestamo','editorial')
    list_display_links = ('tipoMaterial','autor','titulo','anio','status','prestamo','editorial')
    search_fields = ('tipoMaterial','autor','titulo','anio','status','prestamo','editorial')
    fieldsets = (
        ('Descripcion', {
            'fields':('tipoMaterial','autor', 'titulo', 'anio', 'editorial', 'portada')
        }),
        ('Estado', {
            'fields':('status','prestamo',)
        }),
    )

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('tipoMaterial','autor','titulo','anio','status','prestamo')
    list_display_links = ('tipoMaterial','autor','titulo','anio','status','prestamo')
    search_fields = ('tipoMaterial','autor','titulo','anio','status','prestamo')
    fieldsets = (
        ('Descripcion', {
            'fields':('tipoMaterial','autor', 'titulo', 'anio',)
        }),
        ('Estado', {
            'fields':('status','prestamo',)
        }),
    )

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('tipoPersona','matricula','nombre','apellido','telefono','correo','numLibros','adeudo','prestamo')
    list_display_links = ('tipoPersona','matricula','nombre','apellido','telefono','correo','numLibros','adeudo','prestamo')
    search_fields = ('tipoPersona','matricula','nombre','apellido','telefono','correo','numLibros','adeudo','prestamo')
    fieldsets = (
        ('Descripcion', {
            'fields':('tipoPersona','nombre', 'apellido', 'telefono', 'correo')
        }),
        ('Variables', {
            'fields':('matricula','prestamo', 'adeudo', 'numLibros')
        }),
    )

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('tipoPersona','numEmpleado','nombre','apellido','telefono','correo','numLibros','adeudo','prestamo')
    list_display_links = ('tipoPersona','numEmpleado','nombre','apellido','telefono','correo','numLibros','adeudo','prestamo')
    search_fields = ('tipoPersona','numEmpleado','nombre','apellido','telefono','correo','numLibros','adeudo','prestamo')
    fieldsets = (
        ('Descripcion', {
            'fields':('tipoPersona','nombre', 'apellido', 'telefono', 'correo')
        }),
        ('Variables', {
            'fields':('numEmpleado','prestamo', 'adeudo', 'numLibros')
        }),
    )

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
