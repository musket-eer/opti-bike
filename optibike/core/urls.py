from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request/', views.bike_request, name='bike_request'),
    path('options/', views.bike_options, name='bike_options'),
    path('your_bike/', views.your_bike, name='your_request'),
]
