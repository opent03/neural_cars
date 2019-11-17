import pygame
import numpy as np
from game import *
class Car(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.image.load('images/car4.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.prev_pos = (self.rect.x, self.rect.y)
        self.angle = 0
        self.change = 0
    '''
    def update(self):
        if self.change:
            length = np.sqrt((self.rect.x - self.prev_pos[0])**2+(self.rect.y - self.prev_pos[1])**2)
            self.angle = self.angle + (np.sin((self.rect.y - self.prev_pos[1])/length))
            print(self.angle)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.angle = 0
        self.change = 0
    '''
    def moveRight(self, pixels):
        self.change = 1
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.change = 1
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.change = 1
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.change = 1
        self.rect.y += pixels


if __name__ == '__main__':
    print(WHITE)