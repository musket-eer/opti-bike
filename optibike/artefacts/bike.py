import hashlib

class Bike:
    def __init__(self, bike_id, manual_lock_code, rack):
        self.bike_id = bike_id
        self.manual_lock_code = manual_lock_code
        self.user = None
        self.needs_repair = False
        self.rack = rack # type of rack object
        self.is_locked = False

    def assign_user(self, user):
        # assign user to this bike
        self.user = user

    def lock(self):
        self.lock  =True

    def repair(self):
        self.needs_repair = True

    def generate_lock_code(self):
        # Dummy implementation to generate a new lock code
        return "1234"  # Replace with actual implementation

    def update_rack(self, new_rack):
        self.rack = new_rack

        


# Example usage:
bike1 = Bike("ABC123", "5678")
bike1.assign_user("user@example.com")
print(bike1.user_email_map)
print(bike1.rack())
print(bike1.lock())
bike1.repair()
print(bike1.needs_repair)
