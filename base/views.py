
from django.shortcuts import render
from django.views.generic import ListView
from .models import YourModel

class home(ListView):
    model = YourModel
    template_name = 'index.html'
    context_object_name = 'home'

class about(ListView):
    model = YourModel
    template_name = 'about.html'
    context_object_name = 'about'

class gallery(ListView):
    model = YourModel
    template_name = 'gallery.html'
    context_object_name = 'gallery'

