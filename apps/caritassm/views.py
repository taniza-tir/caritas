from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import programas_y_proyectos, boletines, recursos_visuales, ofertas_empleo

class LoginView(TemplateView):
    template_name='login.html'

class HomeView(TemplateView):
    template_name='index.html'

class EvolucionView(TemplateView):
    template_name='evolucion.html'

class ListarProgramas(ListView):
    template_name='programas.html'
    model = programas_y_proyectos

    def get_queryset(self):
        return programas_y_proyectos.objects.all()

class ListarBoletines(ListView):
    template_name='boletines.html'
    model = boletines

    def get_queryset(self):
        return boletines.objects.all()

class ListarRecursos(ListView):
    template_name='recursos.html'
    model = recursos_visuales

    def get_queryset(self):
        return recursos_visuales.objects.all()

class ListarEmpleos(ListView):
    template_name='empleos.html'
    model = ofertas_empleo

    def get_queryset(self):
        return ofertas_empleo.objects.all()

class ContactoView(TemplateView):
    template_name='contacto.html'


# Create your views here.
