
from django.shortcuts import render
from django.views.generic import ListView
from .models import YourModel, Donation

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

class contact(ListView):
    model = YourModel
    template_name = 'contact.html'
    context_object_name = 'contact'

class donation(ListView):
    model = Donation
    template_name = 'donation.html'
    context_object_name = 'donation'


class donationDetail(ListView):
    model = Donation
    template_name = 'donation-details.html'
    context_object_name = 'donation'