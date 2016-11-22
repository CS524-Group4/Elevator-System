from Sensors.Sensor import Sensor


class SpeedSensor(Sensor):
    def _init_(self):
        self.limit = 2.5
        self.health = 100.0
        self.tolerance = 0.5
        self.cur_measure = 0.0

    def is_safe(self):
        if self.cur_measure < self.limit + self.tolerance:
            return True
        else:
            return False