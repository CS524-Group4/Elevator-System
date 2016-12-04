from Sensors.Sensor import Sensor

class Smoke_sensor(Sensor):
    def _init_(self):
        self.smoke = True;

    def isSafe(self):
        if self.smoke == False:
            return False
        else:
            return True


