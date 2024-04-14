class MatchingAlgorithm:
    def __init__(self, bikes):
        self.bikes = bikes  # A list of Bike instances

    def allocate_bikes(self, requests):
        # Sort requests by end time for optimal interval scheduling
        sorted_requests = sorted(requests, key=lambda r: r.end_time)
        user_bike_map = {}

        for request in sorted_requests:
            for bike in self.bikes:
                # Assume each bike has an `is_available` method to check availability for given times
                if not bike.is_locked():
                    # Assume each bike has a `book` method to book the bike
                    bike.lock(request.start_time, request.end_time)
                    if request.user not in user_bike_map:
                        user_bike_map[request.user] = []
                    user_bike_map[request.user].append(bike.bike_id)
                    break  # Break once the first available bike is found and booked

        return user_bike_map
