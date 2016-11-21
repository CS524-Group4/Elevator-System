from Sensors.Sensor import Sensor


class DoorSensor(Sensor):
    def _init_(self):
        self.object = False;

    def isSafe(self):
        if not self.object == False:
            return False
        else:
            return True


