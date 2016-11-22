from Sensors.Sensor import Sensor


class SmokeSensor(Sensor):
    def _init_(self):
        self.cur_measure = False

    def is_safe(self):
        if not self.cur_measure:
            return True
        else:
            return False