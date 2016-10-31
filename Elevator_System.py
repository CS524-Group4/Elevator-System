from queue import PriorityQueue

class ElevatorSystem:
    def __init__(self):
        self.rQueue = PriorityQueue()

    def add_request(self, request):
        self.rQueue.put(request)

    def next_request(self):
        return self.rQueue.get().request

    def is_empty(self):
        if self.rQueue.empty():
            return True
        return False

    def request_size(self):
        return self.rQueue.qsize()

    def go_up(self):
        print("up")

    def go_down(self):
        print("down")