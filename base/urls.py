from django.urls import path
from .views import home,about,gallery,contact,donation,donationDetail

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('about/', about.as_view(), name='about'),
    path('gallery/', gallery.as_view(), name='gallery'),
    path('contact/', contact.as_view(), name='contact'),
    path('donation/', donation.as_view(), name='donation'),
    path('donation-detail/', donationDetail.as_view(), name='donation-detail'),
]