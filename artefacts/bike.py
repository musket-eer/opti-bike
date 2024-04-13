import hashlib

class Bike:
    def __init__(self, bike_id, manual_lock_code):
        self.bike_id = bike_id
        self.manual_lock_code = manual_lock_code
        self.user_email_map = {}  # Maps user email to bike ID
        self.needs_repair = False

    def assign_user(self, user_email):
        # Hash the bike ID and user email for privacy
        hashed_bike_id = hashlib.sha256(self.bike_id.encode()).hexdigest()
        hashed_user_email = hashlib.sha256(user_email.encode()).hexdigest()
        self.user_email_map[hashed_bike_id] = hashed_user_email

    def rack(self):
        # Return a list of bike rack locations (dummy data for demonstration)
        bike_rack_locations = [
            {"latitude": 37.7749, "longitude": -122.4194},  # Example location 1
            {"latitude": 40.7128, "longitude": -74.0060}   # Example location 2
            # Add more locations as needed
        ]
        return bike_rack_locations

    def lock(self):
        # Generate a new manual lock code for the bike
        new_lock_code = self.generate_lock_code()
        # Send the new lock code to the user (not implemented)
        return new_lock_code

    def repair(self):
        # Set the bike to needs repair state
        self.needs_repair = True

    def generate_lock_code(self):
        # Dummy implementation to generate a new lock code
        return "1234"  # Replace with actual implementation

# Example usage:
bike1 = Bike("ABC123", "5678")
bike1.assign_user("user@example.com")
print(bike1.user_email_map)
print(bike1.rack())
print(bike1.lock())
bike1.repair()
print(bike1.needs_repair)
