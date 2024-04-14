from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the homepage")

def bike_request(request):
    return HttpResponse("This is where you request your bike")


    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     location = request.POST.get('location')
    #     time_from = request.POST.get('time_from')
    #     time_to = request.POST.get('time_to')

    #     # Validation or processing here, e.g., checking email validity
    #     if "@edu" not in email:
    #         return HttpResponse("Please use a valid .edu email address.", status=400)

    #     # Assuming you handle the logic to check availability and book the bike here


    #     # Optionally send an email confirmation
    #     send_mail(
    #         'Bike Reservation Confirmation',
    #         f'You have reserved a bike at {location} from {time_from} to {time_to}.',s
    #         settings.EMAIL_HOST_USER)
