from django.contrib import admin
from django.urls import path
from .views import LoginView, HomeView, EvolucionView, ListarProgramas, ListarBoletines, ListarRecursos, ListarEmpleos, ContactoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('index/', HomeView.as_view(), name='home'),
    path('evolucion/', EvolucionView.as_view(), name='evolucion'),
    path('programas/', ListarProgramas.as_view(), name='programas_y_proyectos'),
    path('boletines/', ListarBoletines.as_view(), name='boletines'),
    path('recursos/', ListarRecursos.as_view(), name='recursos'),
    path('empleos/', ListarEmpleos.as_view(), name='empleos'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
   
]
