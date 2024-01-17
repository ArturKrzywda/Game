import pygame as pg 

Playerhight = 85 #y
Playerwidth = 75 #x
image = pg.image.load('Assets\\player.png')

#281
#248


class Player():
    def __init__(self,sc,WIDTH,HIGHT):

        self.WIDTH = WIDTH
        self.HIGHT = HIGHT
        self.screen = sc
        self.rect  = image.get_rect(midbottom = (self.WIDTH/2,850))
    
    def draw(self):
        self.screen.blit(image,self.rect)
    def update(self):
        self.mousepos = pg.mouse.get_pos()
        if self.mousepos != (0,0):
            self.rect.centerx = self.mousepos[0] 
            self.rect.centery = self.mousepos[1] 
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.right > self.WIDTH: self.rect.right = self.WIDTH
        if self.rect.bottom > self.HIGHT: self.rect.bottom = self.HIGHT
 

        
        