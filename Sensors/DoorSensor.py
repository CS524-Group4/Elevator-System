from Sensors.Sensor import Sensor


class DoorSensor(Sensor):
    def _init_(self):
        Sensor.__init__(self)
        self.cur_measure = False

    def is_safe(self):
        if self.cur_measure:
            return False
        else:
            return True


