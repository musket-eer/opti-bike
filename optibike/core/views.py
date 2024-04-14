from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from artefacts import bike

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


def bike_options(request):

    return HttpResponse("here are your options")


#     if request.method == 'POST':
#         bike_id = request.POST.get('bike_id')
#         # Here you would typically handle the bike booking logic
#         return redirect('confirmation_page', bike_id=bike_id)

#     else:  # GET request
#         user_location = request.session.get('user_location', default_location)
#         bikes = bike.objects.filter(is_available=True)
#         # Placeholder for sorting logic - you would implement actual distance calculation here
#         bikes = sorted(bikes, key=lambda x: x.distance_to(user_location))
#         return render(request, 'core/options.html', {'bikes': bikes})

# def calculate_distance(bike_location, user_location):
#     # Dummy function to calculate distances
#     return abs(bike_location - user_location)

def your_bike(request):
    return HttpResponse("here is your bike")
