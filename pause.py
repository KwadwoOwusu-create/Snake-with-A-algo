import pygame,sys
from pygame.locals import*
pygame.init()
class pause:
    def __init__(self, screen) -> None:
        self.checker = True 
        self.font = pygame.font.Font("04B_30__.ttf", 60)
        self.screen = screen
        self.background = screen.fill("black")
        
    #draws text on screen 
    def draw_text(self, text, font, text_col, cords, screen):
        img = font.render(text, True, text_col)
        screen.blit(img,(cords))
    
    #runs the pause screen 
    def run(self):
        while self.checker == False:
            self.background
            
            #draws the pause on screen 
            pause.draw_text(self,"PAUSE", self.font, (0,0,0), (((570//2)), (520//2)), self.screen)
            pause.draw_text(self,"PAUSE", self.font, (255,255,255), (((550//2)), (500//2)), self.screen)
    
            #if space is pressed pause is shown 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.checker = True 
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            pygame.display.update()