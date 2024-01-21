from django.db import models
from django.utils.text import slugify


class Organizador(models.Model):
    id_organizador = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=30, unique=True, blank=False, null=False)
    usuario = models.CharField(max_length=30, unique=True, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre

    def save(self, args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Competidor, self).save(args, **kwargs)

    class Meta:
        verbose_name_plural = "Organizadores"


class Carrera(models.Model):
    estado_carrera = {
        ("0", "Sin Correr"),
        ("1", "finalizada"),

    }
    id_carrera = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=30, unique=True, blank=False, null=False)
    vueltas = models.PositiveIntegerField(blank=False, null=False)
    ubicacion = models.CharField(max_length=40, null=False, blank=False)
    estado = models.CharField(max_length=15, verbose_name='Estado de la carrera', choices=estado_carrera, blank=False)
    fecha = models.DateTimeField(null=False, blank=False, help_text="Fecha y hora de la carrera")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Carreras"


class Equipo(models.Model):
    id_equipo = models.PositiveIntegerField(verbose_name='Clave', primary_key=True, blank=False, null=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=20, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=20, unique=True, blank=False, null=False)
    cantidad_competidores = models.PositiveIntegerField(verbose_name='Cantidad de Competidores', blank=False,
                                                        null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Equipos"


class Competidor(models.Model):
    tipo_sangre = {
        ("1", "A+"),
        ("2", "A-"),
        ("3", "B+"),
        ("4", "B-"),
        ("5", "AB+"),
        ("6", "AB-"),
        ("7", "O+"),
        ("8", "O-")
    }
    id_competidor = models.PositiveIntegerField(verbose_name='Clave', primary_key=True, blank=False, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=30, unique=True, blank=False, null=False)
    direccion = models.CharField(verbose_name='Direccion', max_length=40, null=False, blank=False)
    telefono = models.CharField(verbose_name='Telefono', max_length=10, blank=False, null=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=20, null=False)
    estado = models.CharField(verbose_name='Estado', max_length=20, null=False)
    CURP = models.CharField(verbose_name='CURP', max_length=20, null=False)
    edad = models.PositiveIntegerField(verbose_name='Edad', blank=False, null=False)
    tipo = models.TextField(verbose_name='Tipo de Sangre', choices=tipo_sangre, blank=False)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)  # foreinKey

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Competidores"


class Categoria(models.Model):
    id_categoria = models.PositiveIntegerField(verbose_name='Clave', primary_key=True, blank=False, null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=30, unique=True, blank=False, null=False)
    requisitos = models.TextField(verbose_name='Requisitos', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"


class CarrEqui(models.Model):
    id_carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)  # foreinKey
    id_equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)  # foreinKey
    posicion = models.PositiveIntegerField(verbose_name='Posicion', blank=False, null=False)

    def __str__(self):
        return f"{self.id_carrera} - {self.id_equipo}"

    class Meta:
        verbose_name_plural = "Carrera_Equipo"


class OrgCarr(models.Model):
    id_organizador = models.ForeignKey(Organizador, on_delete=models.PROTECT)  # foreinKey
    id_carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)  # foreinKey

    def __str__(self):
        return f"{self.id_organizador} - {self.id_carrera}"

    class Meta:
        verbose_name_plural = "Organizador_Carrera"


class CompCat(models.Model):
    id_competidor = models.ForeignKey(Competidor, on_delete=models.PROTECT)  # foreinKey
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)  # foreinKey

    def __str__(self):
        return f"{self.id_competidor} - {self.id_categoria}"

    class Meta:
        verbose_name_plural = "Competidor_Categoria"
