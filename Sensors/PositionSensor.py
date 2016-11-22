from Sensors.Sensor import Sensor


class PositionSensor(Sensor):
    def _init_(self):
        self.Difference_In_Position = 0.5; # the differeance between the elevator Surface and the floor surface mesurment in 0.5 centimeter

    def is_safe(self):
        if self.Difference_In_Position <= 0.5:
            return True
        else:
            return False


