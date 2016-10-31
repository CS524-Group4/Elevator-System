class Request:
    def __init__(self, priority, request):
        self.priority = priority
        self.request = request

    def get_priority(self):
        return self.priority

    def get_action(self):
        return self.request

    def get_request(self):
        return (self.priority, self.request)

    def __lt__(self, other):
        self_priority = (self.priority)
        other_priority = (other.priority)
        return self_priority < other_priority

