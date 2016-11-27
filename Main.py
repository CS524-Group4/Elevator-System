import pygame
import os
from time import sleep
from ElevatorSystem import ElevatorSystem


pygame.init()

#Display window size
display_width = 600
display_height = 850

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Elevator')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

sys = ElevatorSystem()
car = sys.get_car()
clock = pygame.time.Clock()
crashed = False
elev_img = pygame.image.load(os.path.abspath("Resources/level 3 elevator.png"))
fore_img = pygame.image.load(os.path.abspath("Resources/all elevator 5 floors.png"))
emergency_text = pygame.font.SysFont("monospace", 80)
waiting_time = 5

#positions of image relative to window
back_x = (display_width * 0.20)
back_y = (display_height*0.0005)
elev_y = (display_height * 0.780)
elev_x = (display_width * 0.320)

#speed of car
y_change = 3
#position to the floor destination
dest_pos = 0
#keeps track of position of elevator
current_pos = 0
#distance between floor
dis_per_floor = 153

#create images in simulation space
def game_object(x, y, img):
    game_display.blit(img, (x, y))

#Displays emergency text if there is an emergency
def check_emergency():
    emergency = sys.get_emergency()
    if emergency:
        label = emergency_text.render("Emergency!", 1, red)
        game_display.blit(label, (100, 100))



#test variables
sys.add_request("move", 5, "firefighter")
sys.add_request("move", 3, "passenger")
sys.add_request("move", 2, "firefighter")
speed = sys.get_sensor_controller().get_speed()
sys.get_sensor_controller().set_sensor_measure(speed, 90)

#Main simulation loop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True

    move = car.get_move()
    print("Move: " + str(move))
    dir = car.get_dir()
    diff = car.get_diff()
    dest_pos = abs(diff * dis_per_floor)

    game_display.fill(white)

    #move function
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
        print("Destination Pos: " + str(dest_pos))
        if current_pos >= dest_pos:
            current_pos = 0
            car.stop()
            pygame.mixer.music.load("Resources/elevator-ding.ogg")
            pygame.mixer.music.play()
            sleep(waiting_time)

    else:
        sys.run()

    game_object(back_x, back_y, fore_img)
    game_object(elev_x, elev_y, elev_img)
    print("Emergency: " + str(sys.get_emergency()))
    check_emergency()


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

