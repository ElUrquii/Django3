from django.db import models

# Create your models here.

class Prestamo(models.Model):
    codigo = models.AutoField(primary_key = True)
    fechaSalida = models.CharField(max_length = 50)
    fechaRegreso = models.CharField(max_length = 50)

    def cuota():
        pass

    def __str__(self):
        return str(self.codigo)

class Material(models.Model):
    codigo = models.AutoField(primary_key = True)
    prestamo = models.ForeignKey('Prestamo', on_delete = models.CASCADE, null = False)
    tipoMaterial = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    titulo = models.CharField(max_length = 30)
    anio = models.IntegerField()
    status = models.CharField(max_length = 30)

    def altaMaterial():
        pass

    def bajaMaterial():
        pass

    def cambioMaterial():
        pass

    def __str__(self):
        return str(self.tipoMaterial)

class Persona(models.Model):
    prestamo = models.OneToOneField('Prestamo', on_delete = models.CASCADE, null = False)
    tipoPersona = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    telefono = models.IntegerField()
    correo = models.CharField(max_length = 30)
    numLibros = models.IntegerField()
    adeudo = models.FloatField()

    def llevarMaterial():
        pass

    def dejarMaterial():
        pass

    def __str__(self):
        return str(self.tipoPersona)

class Libro(Material):
    editorial = models.CharField(max_length = 40)

    def __str__(self):
        return str(Material.titulo)

class Revista(Material):

    def __str__(self):
        return str(Material.titulo)

class Alumno(Persona):
    matricula = models.IntegerField(primary_key = True)

    def __str__(self):
        return str(Persona.nombre)

class Profesor(Persona):
    numEmpleado = models.IntegerField(primary_key = True)

    def __str__(self):
        return str(Persona.nombre)
