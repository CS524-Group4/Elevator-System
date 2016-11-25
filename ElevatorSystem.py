from queue import PriorityQueue
from CarController import CarController
from Request import Request
from Sensors.SensorController import SensorController
from time import sleep


class ElevatorSystem:
    def __init__(self):
        self.rQueue = PriorityQueue()
        self.car = CarController()
        self.sensors = SensorController()
        self.door_time = 3

    def on(self):
        while not self.is_empty():
            self.do_request()

    def add_request(self, request, floor, user):
        if user == "passenger":
            new_request = Request(2, request, floor, user)
        elif user == "operator":
            new_request = Request(1, request, floor, user)
        elif user == "firefighter":
            new_request = Request(0, request, floor, user)
        self.rQueue.put(new_request)

    def __next_request(self):
        return self.rQueue.get()

    def is_empty(self):
        if self.rQueue.empty():
            return True
        return False

    def request_size(self):
        return self.rQueue.qsize()

    #Need to add something here if the elevator is not safe
    def do_request(self):
        if not self.is_empty():
            cur_request = self.__next_request()
            if cur_request.request == "move":
                self.move_elevator(cur_request.floor)
        else:
            print("Waiting for request")

   #make a function to grab current floor
   #request floor every 5 seconds
    def move_elevator(self, floor):
        sleep(self.door_time)
        if self.is_safe():
            self.close_door()
            self.car.move(floor)
            if self.check_sensor("position"):
                self.open_door()
            else:
                print("Not safe to open door")
        else:
            print("Not safe to move")

    def open_door(self):
        self.car.door_open()
        print("Door opened")

    def close_door(self):
        self.car.door_close()
        print("Door closed")

    def get_sensor_controller(self):
        return self.sensors

    def is_safe(self):
        return self.sensors.check_all_sensors()

    def check_sensor(self, sensor):
        measure_sensor = sensor
        if measure_sensor == "position":
            safe = self.sensors.get_pos().is_safe()
        elif measure_sensor == "door":
            safe = self.sensors.get_door().is_safe()
        elif measure_sensor == "weight":
            safe = self.sensors.get_weight().is_safe()
        elif measure_sensor == "smoke":
            safe = self.sensors.get_smoke().is_safe()
        elif measure_sensor == "speed":
            safe = self.sensors.get_speed().is_safe()

        if safe:
            return True
        else:
            return False





