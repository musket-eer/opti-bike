from matching_alg import MatchingAlgorithm

class UserQueue:
    def __init__(self, requests=None):
        self.requests = requests if requests is not None else []

    def add_request(self, request):
        self.requests.append(request)

    def get_sorted_requests(self, sort_by='start'):
        if sort_by == 'start':
            return sorted(self.requests, key=lambda r: r.start_time)
        elif sort_by == 'end':
            return sorted(self.requests, key=lambda r: r.end_time)
        else:
            raise ValueError("Invalid sort_by value. Use 'start' or 'end'.")



matching_alg = MatchingAlgorithm()
matching_alg.add_bike_requester("John")
matching_alg.add_bike_requester("Alice")
matching_alg.add_bike_requester("Bob")
matching_alg.decide_matching()