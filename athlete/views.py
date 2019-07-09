from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import Avg

from .models import athlete, assessment


def index(request):
    num_athletes = 2
    context = {'num_athletes':num_athletes,}
    
    return render(request, 'index.html',context = context)

def athletes(request):

    return HttpResponse('List of Athletes')

def athlete_view(request):

    athlete_data = athlete.objects.filter(guardian = request.user)
    average_data = assessment.objects.filter(IncludeInAverages = True).aggregate(Avg('HeightJump'))
    context = {'athlete_data':athlete_data,
        'average_data':average_data}
    return render(request,'athlete.html',context)


class AthleteListView(ListView):
    model = athlete
    template_name='athletes.html'
    context_object_name = 'athletes'