import pygame
import os
from ElevatorSystem import ElevatorSystem


pygame.init()

#Display window size
display_width = 600
display_height = 850

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Elevator')

black = (0, 0, 0)
white = (255, 255, 255)

sys = ElevatorSystem()
car = sys.get_car()
clock = pygame.time.Clock()
crashed = False
elev_img = pygame.image.load(os.path.abspath("Resources/elevator.png"))
back_img = pygame.image.load(os.path.abspath("Resources/level 2 elevator.png"))

#create images in simulation space
def game_object(x, y, img):
    gameDisplay.blit(img, (x, y))

#positions of image relative to window
back_x = (display_width * 0.20)
back_y = (display_height*0.0005)
elev_y = (display_height * 0.811)
elev_x = (display_width * 0.325)

#speed of car
y_change = 3
#position to the floor destination
dest_pos = 0
#keeps track of position of elevator
current_pos = 0
#distance between floor
dis_per_floor = 153

#test variables
sys.add_request("move", 5, "passenger")
sys.add_request("move", 3, "passenger")
sys.add_request("move", 2, "passenger")

#Main simulation loop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True

            # if event.key == pygame.K_UP:
            #     dest_pos = abs(car.move(5) * dis_per_floor)
            #
            # if event.key == pygame.K_DOWN:
            #     dest_pos = abs(car.move(3) * dis_per_floor)

    move = car.get_move()
    print("Move: " + str(move))
    dir = car.get_dir()

    gameDisplay.fill(white)

    if move:
        if dir == "up":
            elev_y -= y_change
        elif dir == "down":
            elev_y += y_change

        current_pos += y_change

        if current_pos%dis_per_floor == 0:
            if dir == "up":
                current_floor = car.get_floor() + 1
                car.set_floor(current_floor)
            else:
                current_floor = car.get_floor() - 1
                car.set_floor(current_floor)

        if current_pos >= dest_pos:
            current_pos = 0
            car.stop()
    else:
        sys.do_request()

    game_object(back_x, back_y, back_img)
    game_object(elev_x, elev_y, elev_img)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

