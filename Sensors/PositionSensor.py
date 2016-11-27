from Sensors.Sensor import Sensor


class PositionSensor(Sensor):
    def _init_(self):
        Sensor.__init__(self)
        self.limit = 0.5
        self.tolerance = 1

    def is_safe(self):
        if self.cur_measure <= self.limit + self.tolerance:
            return True
        else:
            return False


