from queue import PriorityQueue
from Controller import Car
from Request import Request


class ElevatorSystem:
    def __init__(self):
        self.rQueue = PriorityQueue()
        self.car = Car()

    def add_request(self, request, floor, user):
        if user == "passenger":
            new_request = Request(2, request, floor, user)
        if user == "operator":
            new_request = Request(1, request, floor, user)
        if user == "firefighter":
            new_request = Request(0, request, floor, user)
        self.rQueue.put(new_request)

    def next_request(self):
        return self.rQueue.get()

    def is_empty(self):
        if self.rQueue.empty():
            return True
        return False

    def request_size(self):
        return self.rQueue.qsize()

    def do_request(self):
        cur_request = self.next_request()
        if cur_request.request == "move":
            self.move_elevator(cur_request.floor)

    def move_elevator(self, floor):
        if self.is_safe():
            self.close_door()
            self.car.move_car(floor)
            #add check position sensor
            self.open_door()

    def open_door(self):
        #check position sensor
        self.car.door_open()

    def close_door(self):
        #add check position sensor
        self.car.door_close()

    def is_safe(self):
        return True
