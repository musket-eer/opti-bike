from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from artefacts import bike
from .forms import BicycleRequestForm

def home(request):
    return HttpResponse("This is the homepage")

def bike_request(request):
    if request.method == 'POST':
        form = BicycleRequestForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # Example: send this data to a queue
            return HttpResponse('Request submitted successfully!')
        else:
            return HttpResponse('Invalid form data', status=400)
    else:
        form = BicycleRequestForm()
        return render(request, 'core/request.html', {'form': form})
    



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
