import pygame
from PyQt5 import QtWidgets

from ElevatorGUI import Ui_ProgramForm
from ElevatorSystem import ElevatorSystem

pygame.init()
sys = ElevatorSystem()
GUI = Ui_ProgramForm()
car = sys.get_car()

def sim_loop():
    crashed = False
    clock = pygame.time.Clock()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("hello")

        GUI.move()
        #pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgramForm = QtWidgets.QWidget()
    ui = Ui_ProgramForm()
    ui.setupUi(ProgramForm)
    ProgramForm.show()
    sys.exit(app.exec_())



