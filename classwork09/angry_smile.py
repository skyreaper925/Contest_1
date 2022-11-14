import pygame
from pygame.draw import *

pygame.init()

FPS = 30
size = 400
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 0, 255), (200, 200), 200) #main circle

circle(screen, (255, 255, 255), (125, 175), 50) #outer circles
circle(screen, (255, 255, 255), (275, 175), 50)

circle(screen, (255, 155, 255), (125, 175), 35) #inner circles
circle(screen, (255, 155, 255), (275, 175), 20)

rect(screen, (0, 0, 0), (125, 275, 150, 25)) #mouse

x = 110
y = 90
polygon(screen, (0,0,0), [(x, y), (x+20, y-25), (x+100, y+50), (x+50,y+50)])
# polygon(screen, (150,250,50), [(size-y, size-x), (size-y+20, size-x-25), (size-y+100, size-x+50), (size-y+50,size-x+50)])
polygon(screen, (0,0,0), [(size-x, y), (size-x-20, y-25), (size-x-50, y+50), (size-x-50,y+50)])
# polygon(screen, (220,220,220), [(x, y), (x+20, y-25), (x+100, y+50), (x+50,y+50)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()