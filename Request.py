class Request:
    def __init__(self, priority, request, floor, user):
        self.priority = priority
        self.request = request
        self.floor = floor
        self.user = user

    def get_priority(self):
        return self.priority

    def get_action(self):
        return self.request

    def get_request(self):
        return (self.priority, self.request)

    #Allows the object to be ordered by priority
    def __lt__(self, other):
        self_priority = (self.priority)
        other_priority = (other.priority)
        return self_priority < other_priority

