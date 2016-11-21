from abc import ABC, abstractmethod


class Sensor (ABC):
    def __init__(self):
        self.limit = 0.0
        self.health = 100.0
        self.tolerance = 0.0
        self.cur_measure = 0.0

    @abstractmethod
    def isSafe(self):
        pass

    def set_health(self, health):
        self.health = health

    def set_measure(self, measure):
        self.cur_measure = measure

    def set_tolerance(self, tol):
        self.tolerance = tol




