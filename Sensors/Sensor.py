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

    def setHealth(self, health):
        self.health = health

    def setMeasure(self, measure):
        self.cur_measure = measure

    def setTolerance(self, tol):
        self.tolerance = tol




