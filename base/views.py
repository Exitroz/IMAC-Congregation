
from django.shortcuts import render
from django.views.generic import ListView
from .models import YourModel

class home(ListView):
    model = YourModel
    template_name = 'index.html'
    context_object_name = 'home'

