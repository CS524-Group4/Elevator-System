import pygame
import os
import time
import sys
from PyQt5 import QtWidgets
from ElevatorGUI import ElevatorGUI

pygame.init()


class main():
    def __init__(self):
        self.gui = ElevatorGUI()
        self.first_floor = -69
        self.second_floor = -205
        self.third_floor = -341
        self.fourth_floor = -477
        self.fifth_floor = -613
        self.dis_per_floor = 136
        self.y_change = -1
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.waiting_time = 6
        self.move = False
        self.last = time.time()
        self.sim_loop()
    
    def sim_loop(self):
        app = QtWidgets.QApplication(sys.argv)
        ProgramForm = QtWidgets.QWidget()
        ui = self.gui
        ui.setupUi(ProgramForm)
        ProgramForm.show()

        e_sys = self.gui.get_sys()
        car = self.gui.get_sys().get_car()

        now = 0
    
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        self.crashed = True

            self.update(e_sys,car)

            if self.move:
                self.move_car(car, self.gui.Inside_Elvetor_Car.y())
            else:
                #Waits for the waiting time to run another request
                if now - self.last >= self.waiting_time:
                    e_sys.run()
                else:
                    now = time.time()
    
            self.clock.tick(60)

    def move_car(self, car, elevator_pos):
        if elevator_pos > self.dest_pos:
            self.gui.move(self.y_change)
            elevator_pos = self.gui.Inside_Elvetor_Car.y()
            self.update_floor(elevator_pos, car)
        elif elevator_pos < self.dest_pos:
            self.gui.move(abs(self.y_change))
            elevator_pos = self.gui.Inside_Elvetor_Car.y()
            self.update_floor(elevator_pos, car)
        else:
            car.stop()
            self.last = time.time()
            pygame.mixer.music.load(os.path.abspath("Resources/elevator-ding.ogg"))
            pygame.mixer.music.play()
            self.gui.get_door()

    def update(self, sys, car):
        sys.check_emergency()
        self.move = car.get_move()
        floor = car.get_req_floor()
        if floor is 1:
            self.dest_pos = self.first_floor
        elif floor is 2:
            self.dest_pos = self.second_floor
        elif floor is 3:
            self.dest_pos = self.third_floor
        elif floor is 4:
            self.dest_pos = self.fourth_floor
        elif floor is 5:
            self.dest_pos = self.fifth_floor

    def update_floor(self, pos, car):
        if pos % self.dis_per_floor == 0:
            if pos > self.dest_pos:
                car.set_floor(car.get_floor() + 1)
                self.gui.Update_Display()
            elif pos < self.dest_pos:
                car.set_floor(car.get_floor() - 1)
                self.gui.Update_Display()


main()
