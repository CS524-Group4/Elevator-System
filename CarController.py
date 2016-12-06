
class CarController:

    def __init__(self):
        self.current_floor = 1
        self.speed = 2
        self.is_open = False
        self.is_moving = False
        self.req_floor = 1
        self.direction = "up"

    #Allows car to move and returns difference of floor for car simulation in pygame
    def move(self, floor):
        print("Floor: " + str(floor))
        diff = floor - self.current_floor
        if diff < 0:
            self.is_moving = True
            self.req_floor = floor
        else:
            self.is_moving = True
            self.req_floor = floor

    #Tells when floor is reach
    def floor_reached(self):
        print ("Reached Floor: " + str(self.current_floor))

    def stop(self):# Stop
        self.is_moving = False
        self.floor_reached()

    def car_emergency_stop(self):  # EmergencyStop
        self.floor_reached()

    def door_open(self): # DoorOpen
        self.is_open = False

    def get_door(self):
        return self.is_open

    def door_close(self): # DoorClose
        self.is_open = True

    #Get it to see if the car is moving
    def get_move(self):
        return self.is_moving

    #Checks to see if its moving
    def get_floor(self):
        return self.current_floor

    #Set the current floor
    def set_floor(self, floor):
        self.current_floor = floor
        print("Arriving at Floor: " + str(self.current_floor))

    def get_req_floor(self):
        return self.req_floor

    def set_direction(self, dir):
        self.direction = dir

    def get_direction(self):
        return self.direction

