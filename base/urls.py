from django.urls import path
from .views import home,about,gallery

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('about/', about.as_view(), name='about'),
    path('gallery/', gallery.as_view(), name='gallery'),
]