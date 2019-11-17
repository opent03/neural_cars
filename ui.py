import pygame
from game import *
from game.car import *
dims = (800, 600)


pygame.init()
gameDisplay = pygame.display.set_mode(dims)
pygame.display.set_caption('Racecars')

# load car image
car_image = pygame.image.load('images/car4.jpg')

all_sprites_list = pygame.sprite.Group()

playerCar = Car(70, 40)
all_sprites_list.add(playerCar)

def car(x,y):
    gameDisplay.blit(pygame.transform.scale(car_image, (50,20)), (x,y))


clock = pygame.time.Clock()
crashed = False

while not crashed:
    gameDisplay.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    all_sprites_list.draw(gameDisplay)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)

    if keys[pygame.K_UP]:
        playerCar.moveUp(5)
    if keys[pygame.K_DOWN]:
        playerCar.moveDown(5)

    all_sprites_list.update()

    pygame.display.update()
    clock.tick(60)

pygame.quit()