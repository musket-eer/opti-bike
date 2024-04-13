class Rack:
    def __init__(self, rack_id):
        self.rack_id = rack_id
        self.bikes = set()  # Set to store bike codes
        self.coordinates = {"latitude": None, "longitude": None}  # Coordinates of the rack

    def add_bike(self, bike_code):
        self.bikes.add(bike_code)

    def remove_bike(self, bike_code):
        if bike_code in self.bikes:
            self.bikes.remove(bike_code)

    def update_coordinates(self, latitude, longitude):
        self.coordinates["latitude"] = latitude
        self.coordinates["longitude"] = longitude

# Example usage:
rack1 = Rack("Rack001")

# Add bikes to the rack
rack1.add_bike("001")
rack1.add_bike("002")
rack1.add_bike("003")

print("Bikes in Rack1:", rack1.bikes)

# Remove a bike from the rack
rack1.remove_bike("002")

print("Bikes in Rack1 after removal:", rack1.bikes)

# Update coordinates of the rack
rack1.update_coordinates(37.7749, -122.4194)
print("Coordinates of Rack1:", rack1.coordinates)
