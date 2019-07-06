from django.shortcuts import render
from django.http import HttpResponse

from athlete.models import athlete


def index(request):
    num_athletes = 2
    context = {'num_athletes':num_athletes,}
    
    return render(request, 'index.html',context = context)
