from time import sleep


class CarController:

    def __init__(self):
        self.current_floor = 1
        self.speed = 2
        self.isOpen = False

    def move_car(self, floor):
        diff = floor - self.current_floor
        i = 0;
        if diff == 0:
            print("Still on Floor " + str(self.current_floor))
        if diff < 0:
            diff *= -1
            while i < diff:
                sleep(self.speed)
                self.current_floor -= 1
                i += 1
                print ("On floor: " + str(self.current_floor))
        if diff > 0:
            while i < diff:
                sleep(self.speed)
                self.current_floor += 1
                i += 1
                print ("On floor: " + str(self.current_floor))

        self.stop()

    def floor_reached(self):
        print ("Reached Floor: " + str(self.current_floor))

    def stop(self):# Stop
        self.floor_reached()

    def car_emergency_stop(self):  # EmergencyStop
        self.floor_reached()

    def door_open(self): # DoorOpen
        self.isOpen = False

    def door_close(self): # DoorClose
        self.isOpen = True