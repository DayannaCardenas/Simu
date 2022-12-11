from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.states.models import *

@login_required(login_url='/profiles/login')
def read_states_view(request):
    states=Estado.objects.all()
    context={
                'states':states,
            }
    return render(request, "states/readStates.html",context)