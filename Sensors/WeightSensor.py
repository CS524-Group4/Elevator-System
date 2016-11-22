from Sensors.Sensor import Sensor


class WeightSensor(Sensor):

    def __init__(self):
        Sensor.__init__(self)
        self.limit = 1600.0;
        self.tolerance = 5.0;

    def is_safe(self):
        if self.cur_measure < self.limit + self.tolerance:
            return True
        else:
            return False

