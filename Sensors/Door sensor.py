from Sensors.Sensor import Sensor

class Door_sensor(Sensor):
    def _init_(self):
        self.object = False;

    def isSafe(self):
        if self.object == False:
            return False
        else:
            return True


