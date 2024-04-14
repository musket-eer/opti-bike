class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, bike_requester):
        self.queue.append(bike_requester)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class MatchingAlgorithm:
    def __init__(self):
        self.queue = Queue()

    def add_bike_requester(self, bike_requester):
        self.queue.enqueue(bike_requester)

    def decide_matching(self):
        while not self.queue.is_empty():
            bike_requester = self.queue.dequeue()
            # Perform matching algorithm logic here
            # Decide who can take what bike based on certain criteria
            # You can implement your own logic based on your requirements
            print(f"Matching algorithm: Assigning bike to {bike_requester}")

# Example usage
matching_alg = MatchingAlgorithm()
matching_alg.add_bike_requester("John")
matching_alg.add_bike_requester("Alice")
matching_alg.add_bike_requester("Bob")
matching_alg.decide_matching()