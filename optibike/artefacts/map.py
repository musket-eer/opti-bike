# wraps google maps API.
# is a subset of locations in google maps
# we can use buildings as nodes and distances as edges


import googlemaps

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
    


    # add bike rack. 
