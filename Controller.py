from time import sleep
class Car_conrtroller:

    def __init__(self):
        self.current_floor
        self.speed

    def Car_Move_Up(self):       # MoveUp
        sleep(5)
        self.Car_Current_Floor += 1

    def Car_Move_Down(self):     # MoveDown
        sleep(5)
        self.Car_Current_Floor -= 1

    def floor_reached(self):


    def Car_Move_To(self, floor_number):
        # Move to a specific floor
        while self.Car_Current_Cloor != floor_number:
            if floor_number > self.current_floor:
             # this will only move one floor at a time # we need to say what floor
                f = self.Car_Move_Up()
            else:
                f = self.Car_Move_Down()

        self.floor_reached()

    def Car_Stop(self):# Stop
        self.floor_reached()
    def Car_Emergency_Stop(self):  # EmergencyStop
        self.floor_reached()
    def Car_Door_Open(self): # DoorOpen
        ()

    def Car_Door_Close(self): # DoorClose
        ()