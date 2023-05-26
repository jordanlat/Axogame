import  pygame

class shoot(object):
    def __init__(self, filename, posX, posY, screen):
        self.filename  = filename
        self.type      = pygame.image.load(filename).convert_alpha()
        self.posX      = posX
        self.posY      = posY

        screen.blit(self.type,(posX+60,posY))
        
        #pygame.display.flip()




        
