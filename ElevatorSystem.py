from queue import PriorityQueue
from CarController import CarController
from Request import Request
from Sensors.SensorController import SensorController
from twilio.rest import TwilioRestClient


class ElevatorSystem:
    def __init__(self):
        self.r_queue = PriorityQueue()
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
            new_request = Request(0, request, floor, user)
        elif user == "firefighter":
            new_request = Request(0, request, floor, user)
        self.r_queue.put(new_request)

    #gets next request from queue
    def __next_request(self):
        return self.r_queue.get()

    #checks if queue is empty
    def is_empty(self):
        if self.r_queue.empty():
            return True
        return False

    #gets size of queue
    def request_size(self):
        return self.r_queue.qsize()

    def run(self):
        if not self.emergency:
            self.check_arrival()
            if not self.is_empty() and not self.in_call:
                self.in_call = True
                cur_request = self.__next_request()
                if cur_request.request == "move":
                    self.move_elevator(cur_request.floor, cur_request.user)
            else:
                print("Waiting for request")
        else:
            print("In emergency")

    def reset(self):
        self.emergency = False
        self.in_call = False
        self.sensors.reset_all_sensors()

    #Moves the car
    def move_elevator(self, floor, user):
        if user == "firefighter" or user == "operator":
            self.car.move(floor)
        elif not self.emergency:
            self.close_door()
            self.car.move(floor)

    #Open elevator door
    def open_door(self):
        self.car.door_open()
        print("Door opened")

    #Closes elevator door
    def close_door(self):
        self.car.door_close()
        print("Door closed")

    def get_door(self):
        self.car.get_door()

    #Gets sensor controller
    def get_sensor_controller(self):
        return self.sensors

    #Gets car controller
    def get_car(self):
        return self.car

    #Checks all sensors to see if its safe
    def is_safe(self):
        safe = self.sensors.check_all_sensors()
        if not safe and not self.emergency:
            self.in_emergency()


    #gets current floor
    def get_floor(self):
        return self.car.get_floor()

    #Return emergency flag
    def get_emergency(self):
        return self.emergency

    def check_arrival(self):
        if not self.car.get_move():
            if self.check_sensor("position"):
                self.open_door()
                self.in_call = False

    #Need to figure out how to move to nearest floor during emergencies
    def move_near_floor(self):
        self.in_call = False
        print("Moving to nearest floor: " + str(self.get_floor()))
        self.move_elevator(self.get_floor(), "operator")
        self.emergency = True

    #Checks a specfic sensor
    def check_sensor(self, measure_sensor):
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

    def in_emergency(self):
        self.emergency_call()
        self.r_queue.queue.clear()
        self.move_near_floor()

    def emergency_call(self):
        ACCOUNT_SID = "AC5825ac73a66a689e26884d0eb8090a12"
        AUTH_TOKEN = "cfde9e715e58e1ccc74f52a7ec0fb639"

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        client.messages.create(
            to="+12404467736",
            from_="+12404398153",
            body="There is a emergency with Elevator 1B5 in Hodson Hall, please attend to immediately",
        )





