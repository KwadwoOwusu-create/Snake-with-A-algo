import pygame, random

class food:
    def __init__(self,display_h,display_w,block) -> None:
        self.size = block
        self.color = (186,91,79)
        self.food = pygame.Rect(0,0,self.size,self.size)
        self.eaten = False
        self.display_h,self.display_w = display_h,display_w
        self.food.center = (random.randint(self.size // 2, self.display_w - self.size // 2),random.randint(self.size // 2, self.display_h - self.size // 2))  
        

    
    #repositions food
    def position(self):      
        if self.eaten == True:
            self.food.center = (random.randint(self.size // 2, self.display_w - self.size // 2),random.randint(self.size // 2, self.display_h - self.size // 2))
            
    
    #collision detection            
    def collide(self,snake):
        if self.food.colliderect(snake):
            self.eaten = True
        else:
            self.eaten = False 
            
        return self.eaten
        
            
            
    #draws food  
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.food,0,8)

