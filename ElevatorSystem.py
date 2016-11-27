from queue import PriorityQueue
from CarController import CarController
from Request import Request
from Sensors.SensorController import SensorController


class ElevatorSystem:
    def __init__(self):
        self.rQueue = PriorityQueue()
        self.car = CarController()
        self.sensors = SensorController()
        self.door_time = 3
        self.in_call = False
        self.emergency = False

    #creates and add requests to queue
    def add_request(self, request, floor, user):
        if user == "passenger":
            new_request = Request(2, request, floor, user)
        elif user == "operator":
            new_request = Request(1, request, floor, user)
        elif user == "firefighter":
            new_request = Request(0, request, floor, user)
        self.rQueue.put(new_request)

    #gets next request from queue
    def __next_request(self):
        return self.rQueue.get()

    #checks if queue is empty
    def is_empty(self):
        if self.rQueue.empty():
            return True
        return False

    #gets size of queue
    def request_size(self):
        return self.rQueue.qsize()

    #Need to add something here if the elevator is not safe
    #Does current request of queue
    def run(self):
        print("Call: " + str(self.in_call))
        self.check_movement()
        if not self.is_empty() and not self.in_call:
            self.in_call = True
            cur_request = self.__next_request()
            if cur_request.request == "move":
                self.move_elevator(cur_request.floor)
        else:
            print("Waiting for request")

    #Does moving of car
    def move_elevator(self, floor):
        print("Requested floor: " + str(floor))
        if self.is_safe():
            self.emergency = False
            self.close_door()
            self.car.move(floor)
        else:
            self.emergency = True
            print("Not safe to move")

    #Open elevator door
    def open_door(self):
        self.car.door_open()
        print("Door opened")

    #Closes elevator door
    def close_door(self):
        self.car.door_close()
        print("Door closed")

    #Gets sensor controller
    def get_sensor_controller(self):
        return self.sensors

    #Gets car controller
    def get_car(self):
        return self.car

    #Checks all sensors to see if its safe
    def is_safe(self):
        return self.sensors.check_all_sensors()

    #gets current floor
    def get_floor(self):
        return self.car.get_floor()

    def get_emergency(self):
        return self.emergency

    def check_movement(self):
        if not self.car.get_move() or self.is_safe():
            if self.check_sensor("position"):
                self.open_door()
            else:
                print("Not safe to open door")
            self.in_call = False

    #Checks a specefic sensor
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
            self.emergency = False
            return True
        else:
            self.emergency = True
            return False





