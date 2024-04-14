from artefacts.matching_alg import MatchingAlgorithm


class UserQueue:
    def __init__(self, requests=None):
        self.requests = requests if requests is not None else []
        self.matching_algorithm = MatchingAlgorithm()

    def add_request(self, request):
        self.requests.append(request)

    def get_sorted_requests(self, sort_by='start'):
        return self.matching_algorithm.allocate_bikes(self.requests)

