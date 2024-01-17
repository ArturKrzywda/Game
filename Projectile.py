import pygame as pg 
image = pg.image.load('Assets\\projectile.png')


class Projectile():
    def __init__(self,sc,WIDTH,HIGHT):
        self.WIDTH = WIDTH
        self.HIGHT = HIGHT
        self.speed = 15
        self.screen = sc
        self.rect  = image.get_rect(center = pg.mouse.get_pos())

    def draw(self):
        self.screen.blit(image,self.rect)
    def update(self):
        self.rect.y -= self.speed