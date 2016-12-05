from abc import ABC, abstractmethod


class Sensor (ABC):
    def __init__(self):
        self.limit = 0.0
        self.health = 100.0
        self.tolerance = 0.0
        self.cur_measure = 0.0

    #Checks the limit to find if its safe
    @abstractmethod
    def is_safe(self):
        pass

    #Sets health of sensor
    def set_health(self, health):
        self.health = health

    #Sets current measure
    def set_measure(self, measure):
        self.cur_measure = measure

    #Set tolerance of Sensor
    def set_tolerance(self, tol):
        self.tolerance = tol

    def get_measure(self):
        return self.cur_measure



