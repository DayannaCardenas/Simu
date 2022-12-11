from django.urls import path
from apps.states.views import *

urlpatterns = [
	path('readStates/',read_states_view, name='readStates'),

]
    