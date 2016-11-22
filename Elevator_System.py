from queue import PriorityQueue
from Controller import Car
from Request import Request
from Sensors.SensorController import SensorController


class ElevatorSystem:
    def __init__(self):
        self.rQueue = PriorityQueue()
        self.car = Car()
        self.sensors = SensorController

    def add_request(self, request, floor, user):
        if user == "passenger":
            new_request = Request(2, request, floor, user)
        elif user == "operator":
            new_request = Request(1, request, floor, user)
        elif user == "firefighter":
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
        if not self.is_empty():
            cur_request = self.next_request()
            if cur_request.request == "move":
                self.move_elevator(cur_request.floor)
        else:
            print("Waiting for request")

    def move_elevator(self, floor):
        if self.is_safe():
            self.close_door()
            self.car.move_car(floor)
            self.check_sensor(self, "position")
            self.open_door()

    def open_door(self):
        self.check_sensor(self, "position")
        self.car.door_open()

    def close_door(self):
        self.check_sensor(self, "door")
        self.car.door_close()

    def get_sensor_controller(self):
        return self.sensors

    def is_safe(self):
        safe = self.sensors.check_all_sensors()

    def check_sensor(self, sensor):

        measure_sensor = sensor

        if measure_sensor == "position":
            safe = self.sensors.get_pos().isSafe()
        elif measure_sensor == "door":
            safe = self.sensors.get_door().isSafe()
        elif measure_sensor == "weight":
            safe = self.sensors.get_weight().isSafe()

        if not safe:
            return False;
        else: return True;





