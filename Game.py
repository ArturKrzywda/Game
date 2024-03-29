import pygame as pg 
import Player
import Projectile
import Enemy

class Button():
    def __init__(self,sc,WIDTH,HIGHT):
        self.clicked = False
        self.pressed = False
        self.screen = sc
        self.state = 1
        self.idle = pg.image.load("Assets\\button\\idlestart.png") #1
        self.hover = pg.image.load("Assets\\button\\hoverstart.png") #2
        self.click = pg.image.load("Assets\\button\\clickstart.png") #3
        self.rect = self.idle.get_rect(midtop = (WIDTH/2,700))
        
    def draw(self):
        if self.state == 1:
            self.screen.blit(self.idle,self.rect)
        elif self.state == 2:
            self.screen.blit(self.hover,self.rect)
        elif self.state == 3:
            self.screen.blit(self.click,self.rect)
    def update(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                self.state = 3
                self.pressed = True
            else:
                if self.pressed == True:
                    self.pressed = False
                    self.clicked = True
                self.state = 2
        else:
            self.state = 1
    def isclicked(self):
        if self.clicked:
            return True
        else:
            return False

        


class Game():
    def __init__(self,WIDTH,HIGHT,FPS=60):
        self.WIDTH = WIDTH
        self.HIGHT = HIGHT
        self.speed = 10
        self.font = pg.font.Font("Assets/Font.ttf", 50)
        
        self.gameoverf = self.font.render("Game Over!",True, (52, 77, 99))
        self.resetf = self.font.render("Click Space to restart!",True, (52, 77, 99))

        self.screen = pg.display.set_mode((self.WIDTH,self.HIGHT))
        self.running = 3
        
        pg.display.set_caption('Game')
        self.Button = Button(self.screen,self.WIDTH,self.HIGHT)
        self.run = True
        self.clock = pg.time.Clock()
        self.FPS = FPS


        self.mainmenu = pg.image.load("Assets\\mainmenu.png")

        self.bg = pg.transform.scale(pg.image.load('Assets\\background.png'),(WIDTH,HIGHT))
        self.bg2 = pg.transform.scale(pg.image.load('Assets\\back2.png'),(WIDTH,HIGHT))
        self.bgrect = self.bg.get_rect(topleft = (0,0))
        self.bg2rect = self.bg2.get_rect(topleft = (0,-1000))

    def reset(self):
        self.projectiles = []
        self.enemies = []
        self.score = 0
        self.player = Player.Player(self.screen,self.WIDTH,self.HIGHT)
        self.delay = 30
        self.timer = 0 
        self.enemy_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.enemy_timer,900)

    def DrawGame(self):
        self.back()
        for projectile in self.projectiles:
            projectile.draw()
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.screen.blit(self.score_surf,(self.WIDTH/2-self.score_surf.get_width()/2,5))
        
    def collision(self):
        for enemy in self.enemies:
            for enem in self.enemies:
                if enem.rect.colliderect(enemy) and enem != enemy:
                    self.enemies.remove(enem)
            if self.player.rect.colliderect(enemy.rect):
                self.running = 2
            for projectile in self.projectiles:
                     if projectile.rect.colliderect(enemy.rect):
                         self.enemies.remove(enemy)
                         self.projectiles.remove(projectile)
                         self.score += 1

    def back(self):
        self.screen.blit(self.bg,self.bgrect)
        self.screen.blit(self.bg2,self.bg2rect)
        self.bgrect.y += 3
        self.bg2rect.y += 3
        if self.bgrect.top >= self.HIGHT:
            self.bgrect.y = -1000
        if self.bg2rect.top >= self.HIGHT:
            self.bg2rect.y = -1000    

    def offscreen(self):
        for projectile in self.projectiles:
            if projectile.rect.bottom < 0:
                self.projectiles.remove(projectile)
        for enemy in self.enemies:
            if enemy.rect.top > self.HIGHT:
                self.enemies.remove(enemy)

    def createprojectile(self):
        self.mouseclik = pg.mouse.get_pressed()
        if self.timer <= 0:
            if self.mouseclik[0] == True:
                self.projectiles.append(Projectile.Projectile(self.screen,self.WIDTH,self.HIGHT))
                self.timer = self.delay

    def start(self): 
        self.reset()  
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                if self.running == 1:
                    if event.type == self.enemy_timer:
                        self.enemies.append(Enemy.Enemy(self.screen,self.WIDTH,self.HIGHT))
                
                if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            if self.running == 2:
                                self.reset()
                                self.running = 1
                if self.Button.isclicked():
                    if self.running == 3:
                        self.reset()
                        self.running = 1


            if self.running == 1:
                self.offscreen()
                self.createprojectile()
                self.collision()
                self.timer -= 1

                self.score_surf = self.font.render(str(self.score),True,(57, 67, 77))

                for projectile in self.projectiles:
                    projectile.update()
                for enemy in self.enemies:
                    enemy.update()
                self.player.update()

                self.DrawGame()
                self.clock.tick(self.FPS)
            if self.running == 2:  
                self.screen.fill((54, 176, 207))
                self.screen.blit(self.gameoverf,(self.WIDTH/2-140, 200))
                self.screen.blit(self.resetf,(45, 700))
                self.clock.tick(self.FPS)
            if self.running == 3:
                self.screen.blit(self.mainmenu,(0,0))
                self.Button.update()
                self.Button.draw()

            pg.display.update()
            
