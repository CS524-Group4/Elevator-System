from Sensors import Sensor


class WeightSensor(Sensor):
    def __init__(self):
        self.limit = 1600.0;
        self.health = 100.0;
        self.tolerance = 5.0;
        self.cur_measure = 0.0

    def isSafe(self):
        if self.cur_measure < self.limit + self.tolerance:
            return True
        else:
            return False

