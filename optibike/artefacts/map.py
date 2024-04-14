# wraps google maps API.
# is a subset of locations in google maps
# we can use buildings as nodes and distances as edges


import googlemaps
from datetime import datetime


class Map:
    def __init__(self, api_key):
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)

    def find_nearby_bike_racks(self, user_location):
        # Use Places API to find nearby bike racks
        bike_racks = self.gmaps.places_nearby(user_location, radius=1000, type='bicycle_store')
        return bike_racks['results']

    def get_building_name(self, location):
        # Use reverse geocoding to get the name of the building
        reverse_geocode_result = self.gmaps.reverse_geocode(location)
        return reverse_geocode_result[0]['formatted_address']


    def add_bike_rack(self, name, location):
        """ Add a bike rack with its name and location. Location should be a tuple (lat, lng). """
        self.bike_racks[name] = location

    def get_shortest_path(self, start, end, mode='bicycling'):
        """ Calculate the shortest path between two locations using a specified mode of transport. """
        if start in self.bike_racks and end in self.bike_racks:
            start_location = self.bike_racks[start]
            end_location = self.bike_racks[end]
        else:
            raise ValueError("Start or end location is not defined in bike racks.")

        # Request directions
        now = datetime.now()
        directions_result = self.gmaps.directions(start_location,
                                                  end_location,
                                                  mode=mode,
                                                  departure_time=now)
        
        if not directions_result:
            return None

        # Extract the route information
        route = directions_result[0]['legs'][0]
        duration = route['duration']
        distance = route['distance']
        steps = route['steps']

        return {
            "duration": duration,
            "distance": distance,
            "steps": [s['html_instructions'] for s in steps]
        }



# __________________EXAMPLE USAGE HERE___________________________________________________________________
# Example Usage
api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual Google Maps API key
map_instance = Map(api_key)
map_instance.add_bike_rack('Rack 1', (37.7749, -122.4194))
map_instance.add_bike_rack('Rack 2', (34.0522, -118.2437))

# Get the shortest path
path_info = map_instance.get_shortest_path('Rack 1', 'Rack 2')
print(path_info)
