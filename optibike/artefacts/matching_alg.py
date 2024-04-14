from artefacts.bike import Bike
class MatchingAlgorithm:
    def __init__(self):
        # Initialize bikes with unique IDs and locations
        self.bikes = {
            "001": Bike("001", "123", "edmunds"),
            "002": Bike("002", "456", "norton"),
            "003": Bike("003", "789", "estella")
        }

    def allocate_bikes(self, requests):
        # Sort requests by end time for optimal interval scheduling
        sorted_requests = sorted(requests, key=lambda r: r[3])
        user_bike_map = {}

        for request in sorted_requests:
            for bike_id, bike in self.bikes.items():
                # Check if the bike is available for the requested times
                if not bike.is_bike_locked():
                    bike.lock()
                    if request[0] not in user_bike_map:
                        user_bike_map[request[0]] = []
                    user_bike_map[request[0]].append(bike.bike_id)

        return user_bike_map