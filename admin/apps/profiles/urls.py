from django.urls import path
from apps.profiles.views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
	path('home/',home_view, name='home'),
    path('readTipoDocumento/', read_tipoDocumento_view, name='readTipoDocumento'),
    path('createEstudiante/',create_estudiante_view, name='createEstudiante'),
    path('updateEstudiante/<int:pk>',update_estudiante_view, name='updateEstudiante'),
	path('readEstudiante/',read_estudiante_view, name='readEstudiante'),
	path('readEstudiante/<int:pk>',read_estudiante_view, name='readEstudiante'),

]