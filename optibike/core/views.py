from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from artefacts import bike, email_verifier, queue
from .forms import BicycleRequestForm


GLOBAL_QUEUE = queue.UserQueue()

def home(request):
    return HttpResponse("This is the homepage")

def bike_request(request):
    if request.method == 'POST':
        form = BicycleRequestForm(request.POST)
        print(form)
        if form.is_valid():
            verifier = email_verifier.EmailVerifier()

            # Process the data in form.cleaned_data
            # Example: send this data to a queue
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            time_from = form.cleaned_data['time_from']
            time_to = form.cleaned_data['time_to']
            print(email, location, time_from, time_to, " \n")
            print("just before we verify the email")
            if verifier.verify_email(email):
                GLOBAL_QUEUE.add_request((email, location, time_from, time_to))

                return redirect('/options')
            else:
                return HttpResponse('Invalid email')
        else:
            print(form.errors)
            return HttpResponse('Invalid form data', status=400)
    else:
        form = BicycleRequestForm()
        print("form not filled")
        return render(request, 'core/request.html', {'form': form})
    



def bike_options(request):
    bike_options = GLOBAL_QUEUE.get_sorted_requests()
    print(bike_options)
    return render(request, 'options.html', {'bike_options': bike_options})



def your_bike(request):
    return HttpResponse("here is your bike")
