class Lock:
    @staticmethod
    def toggle(bike, locked):
        bike.locked = locked



# Example usage:
class Bike:
    def __init__(self, bike_id):
        self.bike_id = bike_id
        self.locked = False  # Initially unlocked

bike1 = Bike("ABC123")
print("Bike 1 Locked Status:", bike1.locked)

# Lock the bike using the Lock class
Lock.toggle(bike1, True)
print("Bike 1 Locked Status:", bike1.locked)

# Unlock the bike using the Lock class
Lock.toggle(bike1, False)
print("Bike 1 Locked Status:", bike1.locked)
