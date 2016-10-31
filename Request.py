class Request:
    def __init__(self, priority, request, floor, user):
        self.priority = priority
        self.request = request
        self.floor = floor
        self.user = user

    #Allows the object to be ordered by priority
    def __lt__(self, other):
        self_priority = (self.priority)
        other_priority = (other.priority)
        return self_priority < other_priority

