from Sensors.Sensor import Sensor


class SpeedSensor(Sensor):
    def _init_(self):
        Sensor.__init__(self)
        self.limit = 2.5
        self.tolerance = 0.5

    def is_safe(self):
        if self.cur_measure <= self.limit + self.tolerance:
            return True
        else:
            return False