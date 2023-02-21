import pygame 
import os 
import random

WIDTH,HEIGHT= 900,600
WIN= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DVD logo screensaver")
FPS= 60
DVD_WIDTH, DVD_HEIGHT= 270,150
DVD_IMAGE= pygame.image.load("DVD_logo.png")
DVD= pygame.transform.scale(DVD_IMAGE,(DVD_WIDTH,DVD_HEIGHT))

class obj:
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.x_vel= 3
        self.y_vel= 3
    def move(self):
        self.y += self.y_vel
        self.x += self.x_vel
    def set_vel(self,x_vel,y_vel):
        self.x_vel= x_vel 
        self.y_vel= y_vel
    def draw(self):
        WIN.blit(DVD, (self.x, self.y))

def draw(obj):
    WIN.fill("black")
    obj.draw()
    pygame.display.update()

def dvd_collision(dvd):
    if dvd.x < 0 or dvd.x + DVD_WIDTH > WIDTH:
        dvd.set_vel(dvd.x_vel*-1,dvd.y_vel)
    if dvd.y + DVD_HEIGHT > HEIGHT or dvd.y < 0:
        dvd.set_vel(dvd.x_vel,dvd.y_vel*-1)    

def main():
    start_x= random.randint(0,WIDTH/2)
    start_y= random.randint(0,HEIGHT/2)
    dvd= obj(start_x, start_y)
    run= True
    clock= pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                break
        dvd_collision(dvd)
        dvd.move()
        draw(dvd)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()