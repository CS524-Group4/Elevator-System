from time import sleep


class CarController:

    def __init__(self):
        self.current_floor = 1
        self.speed = 2
        self.is_open = False
        self.is_moving = False

    def move(self, floor):
        diff = floor - self.current_floor
        i = 0;
        if diff == 0:
            print("Still on Floor " + str(self.current_floor))
        if diff < 0:
            diff *= -1
            self.is_moving = True
            while i < diff:
                sleep(self.speed)
                self.current_floor -= 1
                i += 1
                print ("On floor: " + str(self.current_floor))
        if diff > 0:
            self.is_moving = True
            while i < diff:
                sleep(self.speed)
                self.current_floor += 1
                i += 1
                print ("On floor: " + str(self.current_floor))

        self.stop()

    def floor_reached(self):
        print ("Reached Floor: " + str(self.current_floor))

    def stop(self):# Stop
        #self.is_moving = False
        self.floor_reached()

    def car_emergency_stop(self):  # EmergencyStop
        self.floor_reached()

    def door_open(self): # DoorOpen
        self.is_open = False

    def door_close(self): # DoorClose
        self.is_open = True

    def get_move(self):
        return self.is_moving