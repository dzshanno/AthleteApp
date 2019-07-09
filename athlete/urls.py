from django.urls import path
from .views import AthleteListView
from . import views

urlpatterns = [
    path('', AthleteListView.as_view(), name='Home'),
    path('athletes/', views.athletes, name='Athletes'),
    path('athlete/', views.athlete_view, name='Athlete'),
]