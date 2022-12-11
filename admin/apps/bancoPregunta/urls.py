from django.urls import path
from apps.bancoPregunta.views import *


urlpatterns = [

    path('readResultados/', read_resultado_view, name='readResultados'),
    path('createPregunta/', create_pregunta_view, name='createPregunta'),
    path('updatePregunta/<int:pk>',update_pregunta_view, name='updatePregunta'),
	path('readPregunta/',read_pregunta_view, name='readPregunta'),
	path('readPregunta/<int:pk>',read_pregunta_view, name='readPregunta'),
    path('readRespuestas/',read_respuestas_view, name='readRespuestas'),


    
]