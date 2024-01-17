import pygame as pg 
import Game

pg.init()

WIDTH = 563
HIGHT = 1000    

def main():
    game = Game.Game(WIDTH,HIGHT)
    game.start()
    pg.quit()

if __name__=='__main__':
    main()




