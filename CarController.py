
class CarController:

    def __init__(self):
        self.current_floor = 1
        self.speed = 2
        self.is_open = False
        self.is_moving = False
        self.dir = "up"

    def move(self, floor):
        diff = floor - self.current_floor
        print("difference: " + str(diff))
        if diff == 0:
            self.stop()
            return 0
        elif diff < 0:
            print("Going down")
            self.is_moving = True
            self.dir = "down"
            return diff
        else:
            print("Going up")
            self.is_moving = True
            self.dir = "up"
            return diff

    def floor_reached(self):
        print ("Reached Floor: " + str(self.current_floor))

    def stop(self):# Stop
        self.is_moving = False
        self.floor_reached()

    def car_emergency_stop(self):  # EmergencyStop
        self.floor_reached()

    def door_open(self): # DoorOpen
        self.is_open = False

    def door_close(self): # DoorClose
        self.is_open = True

    def get_move(self):
        return self.is_moving

    def get_floor(self):
        return self.current_floor

    def set_floor(self, floor):
        self.current_floor = floor
        print("Arriving at Floor: " + str(self.current_floor))

    def get_dir (self):
        return self.dir

    def set_dir(self, dir):
        self.dir = dir

