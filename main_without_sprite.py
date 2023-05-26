import pygame
from pygame.locals import *
import math
import hero_shoot

clock = pygame.time.Clock()
FrameHeight = 600
FrameWidth = 1200
charaX, charaY = 10, FrameHeight/2

pygame.init()
pygame.display.set_caption("AXOLOTO GAME")
screen = pygame.display.set_mode((FrameWidth,FrameHeight))

bg = pygame.image.load('src/newBg.png').convert()
h_shoot_img = pygame.image.load('src/hero_proj.png').convert_alpha()

scroll = 0

tiles = math.ceil(FrameWidth / bg.get_width()) + 1
axo_img = pygame.image.load('src/axo.png').convert_alpha()


def h_shoot(posX,posY, screen):
    hero_shoot.shoot('src/hero_proj.png', posX, posY, True, screen)



running = True
while running:
    #réglage fps
    clock.tick(60)

    # Gère le background
    i = 0
    while(i<tiles):
        screen.blit(bg, (bg.get_width()*i + scroll, 0))
        i+=1
    scroll -= 6

    if abs(scroll) > bg.get_width():
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        charaX -= 4
    if keys[pygame.K_d]:
        charaX += 4
    if keys[pygame.K_z]:
        charaY -= 4
    if keys[pygame.K_s]:
        charaY += 4
    if keys[pygame.K_SPACE]:
        hero_shoot.shoot('src/hero_proj.png', charaX, charaY, screen)
        #h_shoot(charaX,charaY, screen, 1200)

   
    #Permet de bouger le personnage avec la souris
    #charaX, charaY = pygame.mouse.get_pos()

    # Main chara
    screen.blit(axo_img, (charaX, charaY))

    pygame.display.update()


pygame.quit()
