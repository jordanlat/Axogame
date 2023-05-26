import pygame
from pygame.locals import *
import math
from spriteStripAnim import SpriteStripAnim 

clock = pygame.time.Clock()
FrameHeight = 600
FrameWidth = 1200
charaX, charaY = 10, FrameHeight/2

pygame.init()
pygame.display.set_caption("AXOLOTO GAME")
screen = pygame.display.set_mode((FrameWidth,FrameHeight))

bg = pygame.image.load('src/newBg.png').convert()

scroll = 0

tiles = math.ceil(FrameWidth / bg.get_width()) + 1

FPS = 60
frames = FPS / 12

strips = [
    SpriteStripAnim("src/hero_sheet.png", (0,0, 64, 64), 4, 0, True, frames),
    SpriteStripAnim("src/hero_sheet.png", (64,0, 64, 64), 4, 0, True, frames),
    SpriteStripAnim("src/hero_sheet.png", (128,0, 64, 64), 4, 0, True, frames),
    SpriteStripAnim("src/hero_sheet.png", (172,0, 64, 64), 4, 0, True, frames)
]

n = 0
strips[n].iter()
character = strips[n].next()


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

    # Permet de fermer le programme 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # Permet de déplacer le personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        charaX -= 4
    if keys[pygame.K_d]:
        charaX += 4
    if keys[pygame.K_z]:
        charaY -= 4
    if keys[pygame.K_s]:
        charaY += 4

    #Permet de bouger le personnage avec la souris
    #charaX, charaY = pygame.mouse.get_pos()

    # Main chara
    screen.blit(character, (charaX,charaY))
    character = strips[n].next()

    pygame.display.flip()

pygame.quit()
