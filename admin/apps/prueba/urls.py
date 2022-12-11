from django.urls import path
from apps.prueba.views import *
# from apps.locations.apiViews import *

urlpatterns = [
    path('readMateria/', read_materia_view, name='readMateria'),
    path('readGrado/', read_grado_view, name='readGrado'),
    # path('readDepartament/', read_departament_view, name='readDepartament'),
    # path('readCity/', read_city_view, name='readCity'),
    # path('readOffice/', read_office_view, name='readOffice'),
    # path('createOffice/',create_office_view, name='createOffice'),
	# path('updateOffice/<int:pk>',update_office_view, name='updateOffice'),
    #------------URLS APIS----------------------------------------------
	# path('apiDepartament',api_departament, name='apiDepartament'),
	# path('apiCity',api_city, name='apiCity'),
    # path('apiOffice',api_office, name='apiOffice'),
    # path('apiOffice/<int:pk>',api_office, name='apiOffice'),

    
]