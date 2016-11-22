from Sensors.DoorSensor import DoorSensor
from Sensors.PositionSensor import PositionSensor
from Sensors.WeightSensor import WeightSensor
from Sensors.SmokeSensor import SmokeSensor
from Sensors.SpeedSensor import SpeedSensor


class SensorController ():
    def __init__(self):
        self.door_sensor = DoorSensor()
        self.pos_sensor = PositionSensor()
        self.weight_sensor = WeightSensor()
        self.speed_sensor = SpeedSensor()
        self.smoke_sensor = SmokeSensor()
        self.sensors = [self.door_sensor, self.pos_sensor, self.weight_sensor, self.speed_sensor, self.smoke_sensor]

    def check_all_sensors(self):
        for x in self.sensors:
            safe = x.is_safe()
            print(safe)
            if not safe:
                return False;
        return True

    def check_sensor(self, sensor):
        safe = sensor.is_safe()
        if not safe:
            return True
        return False

    def set_sensor_health(self, sensor, health):
        sensor.set_health(health)

    def set_sensor_measure(self, sensor, measure):
         sensor.set_measure(measure)

    def set_sensor_tolerance (self, sensor, tol):
        sensor.set_tolerance(tol)

    def get_door(self):
        return self.door_sensor

    def get_pos(self):
        return self.pos_sensor

    def get_weight(self):
        return self.weight_sensor

    def get_speed(self):
        return self.speed_sensor

    def get_smoke(self):
        return self.smoke_sensor



