from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import athlete


def index(request):
    num_athletes = 2
    context = {'num_athletes':num_athletes,}
    
    return render(request, 'index.html',context = context)

def athletes(request):

    return HttpResponse('List of Athletes')

def athlete_view(request):


    athlete_data = athlete.objects.filter(guardian = request.user)
    return render(request,'athlete.html',{'athlete_data':athlete_data})


class AthleteListView(ListView):
    model = athlete
    template_name='athletes.html'
    context_object_name = 'athletes'