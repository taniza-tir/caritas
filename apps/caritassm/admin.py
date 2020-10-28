from django.contrib import admin
from .models import donantes, municipios, tipologia, programas_y_proyectos, boletines, recursos_visuales, ofertas_empleo
# Register your models here.

admin.site.register(donantes)
admin.site.register(municipios)
admin.site.register(tipologia)
admin.site.register(programas_y_proyectos)
admin.site.register(boletines)
admin.site.register(recursos_visuales)
admin.site.register(ofertas_empleo)


