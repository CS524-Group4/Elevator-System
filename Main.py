import pygame
import os
from time import sleep
from ElevatorSystem import ElevatorSystem
from GUI import ElevatorGUI


pygame.init()

GUI = ElevatorGUI()
sys = ElevatorSystem()
car = sys.get_car()
clock = pygame.time.Clock()
crashed = False

#speed of car
y_change = 3
#position to the floor destination
dest_pos = 0
#keeps track of position of elevator
current_pos = 0
#distance between floor
dis_per_floor = 136

#test variables
# sys.add_request("move", 5, "firefighter")
# sys.add_request("move", 3, "passenger")
# sys.add_request("move", 2, "firefighter")

#Main simulation loop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True
            if event.key == pygame.K_DOWN:
                print("Going down")
                #speed = sys.get_sensor_controller().get_speed()
                #sys.get_sensor_controller().set_sensor_measure(speed, 90)

    # move = car.get_move()
    # print("Move: " + str(move))
    # dir = car.get_dir()
    # diff = car.get_diff()
    # dest_pos = abs(diff * dis_per_floor)
    #
    # #move function
    # if move:
    #     sys.safe_movement()
    #     if dir == "up":
    #         print("Going down")
    #     elif dir == "down":
    #         print("Going up")
    #
    #     current_pos += y_change
    #
    #     if current_pos%dis_per_floor == 0:
    #         print("Floor: ")
    #         if dir == "up":
    #             current_floor = car.get_floor() + 1
    #             print("Current Floor: " + str(current_floor))
    #             car.set_floor(current_floor)
    #         else:
    #             current_floor = car.get_floor() - 1
    #             car.set_floor(current_floor)
    #
    #     if current_pos >= dest_pos:
    #         current_pos = 0
    #         car.stop()
    #         pygame.mixer.music.load("Resources/elevator-ding.ogg")
    #         pygame.mixer.music.play()

    else:
        sys.run()

    clock.tick(60)

pygame.quit()
quit()

