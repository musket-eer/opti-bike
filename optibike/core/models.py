from django.db import models

from django.db import models
import hashlib

class Bike(models.Model):
    bike_id = models.CharField(max_length=255, unique=True)  # Assuming bike IDs are unique strings
    manual_lock_code = models.CharField(max_length=255)  # Store the lock code as a string
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)  # Link to a user model, nullable
    needs_repair = models.BooleanField(default=False)
    rack = models.ForeignKey('Rack', on_delete=models.CASCADE)  # Assuming a Rack model exists
    is_locked = models.BooleanField(default=False)

    def assign_user(self, user):
        # Assign user to this bike
        self.user = user

    def lock(self):
        self.is_locked = True
        self.save()

    def repair(self):
        self.needs_repair = True
        self.save()

    def generate_lock_code(self):
        # Dummy implementation to generate a new lock code
        # Here you would include the actual implementation
        return "1234"  # Replace with actual implementation

    def update_rack(self, new_rack):
        self.rack = new_rack
        self.save()

    def is_bike_locked(self):
        return self.is_locked



class Rack(models.Model):
    rack_id = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # This method creates a human-readable string from the model instance.
    def __str__(self):
        return f"Rack {self.rack_id} at coordinates ({self.latitude}, {self.longitude})"
