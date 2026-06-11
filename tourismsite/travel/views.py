from django.shortcuts import render
from .models import Booking, Contact


def home(request):
    return render(request, 'travel/home.html')


def about(request):
    return render(request, 'travel/about.html')


def destinations(request):
    return render(request, 'travel/destinations.html')


def gallery(request):
    return render(request, 'travel/gallery.html')


def packages(request):
    return render(request, 'travel/packages.html')

def booking(request):
    if request.method == "POST":
        Booking.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            destination=request.POST.get('destination'),
            travel_date=request.POST.get('travel_date')
        )
        return render(request, 'travel/booking.html', {'success': True})

    return render(request, 'travel/booking.html')


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return render(request, 'travel/contact.html', {'success': True})

    return render(request, 'travel/contact.html')



      