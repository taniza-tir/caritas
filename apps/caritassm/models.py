from django.db import models

class donantes(models.Model):
    nombre = models.CharField(max_length=60)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class municipios(models.Model):
    nombre = models.CharField(max_length=60)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class tipologia(models.Model):
    nombre = models.CharField(max_length=60)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class ofertas_empleo(models.Model):
    nombre = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="empleos", null=True)
    def __str__(self):
        return '%s' % (self.nombre)

class boletines(models.Model):
    nombre = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="boletines", null=True)
    ubicacion = models.CharField(max_length=500, default="")
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)


class recursos_visuales(models.Model):
    nombre = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=500, default="")
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)




class programas_y_proyectos(models.Model):
    nombre = models.CharField(max_length=60)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    donante = models.ManyToManyField(donantes)
    costo = models.IntegerField()
    municipio = models.ManyToManyField(municipios)
    area_intervencion = models.CharField(max_length=800)
    tipologia = models.ManyToManyField(tipologia)
    beneficiarios = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=800)
    resultados_esperados = models.CharField(max_length=900)
    resultados_alcanzados = models.CharField(max_length=900)
    acciones_realizadas = models.CharField(max_length=1000)
    metodo_implementado = models.CharField(max_length=1000)
    factores_positivos = models.CharField(max_length=1000)
    factores_negativos = models.CharField(max_length=1000)
    lecciones_aprendidas = models.CharField(max_length=1200)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)
     
