import pygame
import os
import datetime
from datetime import timedelta
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
        self.last = datetime.datetime.now()
        self.warning_time = 3
        self.sim_loop()
    
    def sim_loop(self):
        app = QtWidgets.QApplication(sys.argv)
        ProgramForm = QtWidgets.QWidget()
        ui = self.gui
        ui.setupUi(ProgramForm)
        ProgramForm.show()

        e_sys = self.gui.get_sys()
        car = self.gui.get_sys().get_car()
        self.gui.open_door()
        now = datetime.datetime.now()
    
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
                if now - self.last >= timedelta(seconds=self.waiting_time):
                    if not e_sys.safe_boarding():
                        self.last = datetime.datetime.now() + timedelta(seconds=self.warning_time)
                        pygame.mixer.music.load(os.path.abspath("Resources/crazy-bell.ogg"))
                        pygame.mixer.music.play()
                    else:
                        e_sys.run()


                now = datetime.datetime.now()

    
            self.clock.tick(60)

    def move_car(self, car, elevator_pos):
        self.gui.close_door()
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
            self.gui.open_door()
            self.last = datetime.datetime.now()
            pygame.mixer.music.load(os.path.abspath("Resources/elevator-ding.ogg"))
            pygame.mixer.music.play()

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
