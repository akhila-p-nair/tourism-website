from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('packages/', views.packages, name='packages'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('cancel/<int:booking_id>/',views.cancel_booking,name='cancel_booking'),
]