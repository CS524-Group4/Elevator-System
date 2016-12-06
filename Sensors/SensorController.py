from Sensors.DoorSensor import DoorSensor
from Sensors.PositionSensor import PositionSensor
from Sensors.WeightSensor import WeightSensor
from Sensors.SmokeSensor import SmokeSensor
from Sensors.SpeedSensor import SpeedSensor
from twilio.rest import TwilioRestClient


class SensorController ():
    def __init__(self):
        self.door_sensor = DoorSensor()
        self.pos_sensor = PositionSensor()
        self.weight_sensor = WeightSensor()
        self.speed_sensor = SpeedSensor()
        self.smoke_sensor = SmokeSensor()
        self.sensors = [self.door_sensor, self.pos_sensor, self.weight_sensor, self.speed_sensor, self.smoke_sensor]

    def check_all_sensors(self):
        try:
            for x in self.sensors:
                safe = x.is_safe()
                if not safe:
                    return False

            return True

        except TypeError:
            print("Type Error")
            return False

        except ValueError:
            print("Val Error")
            return False

    def reset_all_sensors(self):
        for x in self.sensors:
            self.reset_sensor(x)

    def check_emergency_sensors(self):
        try:
            if self.speed_sensor.is_safe() and self.smoke_sensor.is_safe() and self.pos_sensor.is_safe():
                return True
            else:
                return False

        except TypeError:
            print("Type Error")
            return False

        except ValueError:
            print("Val Error")
            return False

    def check_boarding_sensors(self):
        try:
            print("is safe: " + str(self.weight_sensor.is_safe()))
            if self.weight_sensor.is_safe() and self.door_sensor.is_safe():
                return True
            else:
                return False

        except TypeError:
            print("Type Error")
            return False

        except ValueError:
            print("Val Error")
            return False


    def set_sensor_health(self, sensor, health):
        sensor.set_health(health)

    def set_sensor_measure(self, sensor, measure):
         try :
             sensor.set_measure(measure)

         except ValueError:
             print("Measure is wrong(Value)")

         except TypeError:
              print ("Measure is wrong(Type)")



    def set_sensor_tolerance (self, sensor, tol):
        try:
            sensor.set_tolerance(tol)

        except ValueError:
            print("Tolerance is wrong(Value)")

        except TypeError:
            print("Tolerance is wrong(Type)")

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

    def warning_text(self):

        text = "Warning: "
        if not self.speed_sensor.is_safe():
            text += "Elevator is going too fast;"
        if not self.smoke_sensor.is_safe():
            text += "There is a fire in the elevator;"
        if not self.pos_sensor.is_safe():
            text+= "The car is out of alignment with the floor;"

        ACCOUNT_SID = "AC5825ac73a66a689e26884d0eb8090a12"
        AUTH_TOKEN = "cfde9e715e58e1ccc74f52a7ec0fb639"

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        client.messages.create(
            to="+12404467736",
            from_="+12404398153",
            body=text,
        )


    def reset_sensor(self, sensor):
        try:
            sensor.set_health(100)
            if type(sensor) is SmokeSensor or type(sensor) is DoorSensor:
                sensor.set_measure(False)
            else:
                sensor.set_measure(0.0)

        except TypeError:
            print("Error in Reset Sensor(Type)")

        except ValueError:
            print("Error in Reset Sensor(Value)")





