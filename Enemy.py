import pygame as pg
import random 
b = 59

image = pg.image.load('Assets\\enemy.png')

class Enemy:
    def __init__(self,sc,WIDTH,HIGHT):
        self.WIDTH = WIDTH
        self.HIGHT = HIGHT
        self.screen = sc
        
        self.rect = image.get_rect(bottomleft = (random.randint(0,self.WIDTH-b),random.randrange(100,500)*-1))

    def draw(self):
        self.screen.blit(image,self.rect)
    def update(self):
        self.rect.y += 3

    def __del__(self):
        pass