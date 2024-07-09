import pygame,random

random1 = random.randint(0,255)
random2 = random.randint(0,255)
random3 = random.randint(0,255)
class snake:
    def __init__(self,block_size):
        self.block_size = block_size
        #random color for the snake
        self.color = (random1,random2,random3)
        #size of the snake
        self.size = block_size
        #head of snake
        self.snake_head = (pygame.Rect(800/2,600/2,self.size,self.size))
        #body of snake
        self.snake_body = [pygame.Rect(800/2 - block_size, 600/2 ,self.size,self.size)]
        #speed of snake
        self.speed = self.size 
        #boolean for alive or death
        self.dead = False
        self.xdirection = 0
        self.ydirection = 0
    
    #renders head   
    def draw_head(self,screen):
        pygame.draw.rect(screen,self.color,(self.snake_head),0,8)
    
    #renders body
    def draw_body(self,screen):
        for snake in range(len(self.snake_body)):
            pygame.draw.rect(screen,self.color,(self.snake_body[snake]),0,8)
            
        
    
    #movement and keys
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.ydirection != 1:
            self.xdirection, self.ydirection = 0, -1
        elif keys[pygame.K_s] and self.ydirection != -1:
            self.xdirection, self.ydirection = 0, 1
        elif keys[pygame.K_a] and self.xdirection != -1:
            self.xdirection, self.ydirection = 1, 0
        elif keys[pygame.K_d]and self.xdirection != 1:
            self.xdirection, self.ydirection = -1, 0
            
    #TODO at something for when the prediction cant predict based on some actions 
    #ai for the snake
    def ai_snake(self, food_pos_x, food_pos_y):
        #a funtion that creats a new rect
        def will_collide_with_body(next_x, next_y):
            next_head = pygame.Rect(next_x, next_y, self.size, self.size)
            #iterates throught the body and if any of the body parts collides 
            # with the new rect it returns true
           
            return any(next_head.colliderect(body_part) for body_part in self.snake_body)

        # Calculate the absolute difference in X and Y positions
        dx = abs(food_pos_x - self.snake_head.x)
        dy = abs(food_pos_y - self.snake_head.y)

        # Determine the primary axis of movement (X or Y) based on which difference is smaller
        if dx > dy:
            primary_axis = 'x'
        else:
            primary_axis = 'y'

        # Try moving in the primary axis direction first
        if primary_axis == 'x':
            if food_pos_x > self.snake_head.x and not will_collide_with_body(self.snake_head.x + self.size, self.snake_head.y):
                self.xdirection, self.ydirection = -1, 0
            elif food_pos_x < self.snake_head.x and not will_collide_with_body(self.snake_head.x - self.size, self.snake_head.y):
                self.xdirection, self.ydirection = 1, 0
            else:
                if food_pos_y > self.snake_head.y and not will_collide_with_body(self.snake_head.x, self.snake_head.y + self.size):
                    self.xdirection, self.ydirection = 0, 1
                elif food_pos_y < self.snake_head.y and not will_collide_with_body(self.snake_head.x, self.snake_head.y - self.size):
                    self.xdirection, self.ydirection = 0, -1
        else:
            if food_pos_y > self.snake_head.y and not will_collide_with_body(self.snake_head.x, self.snake_head.y + self.size):
                self.xdirection, self.ydirection = 0, 1
            elif food_pos_y < self.snake_head.y and not will_collide_with_body(self.snake_head.x, self.snake_head.y - self.size):
                self.xdirection, self.ydirection = 0, -1
            else:
                if food_pos_x > self.snake_head.x and not will_collide_with_body(self.snake_head.x + self.size, self.snake_head.y):
                    self.xdirection, self.ydirection = 1, 0
                elif food_pos_x < self.snake_head.x and not will_collide_with_body(self.snake_head.x - self.size, self.snake_head.y):
                    self.xdirection, self.ydirection = -1, 0    
    
           

                
                    
    #movement for stacking snake bodies
    def update(self):
        self.snake_body.append(self.snake_head)
        for i in range(len(self.snake_body)-1):
            self.snake_body[i].x,self.snake_body[i].y = self.snake_body[i+1].x,self.snake_body[i+1].y
        
        self.snake_head.x-=self.xdirection *self.speed 
        self.snake_head.y+=self.ydirection *self.speed 
        self.snake_body.remove(self.snake_head)
        
    #grows body  
    def grow(self):
        self.snake_body.append(pygame.Rect(self.snake_head.x,self.snake_head.y,self.size,self.size))
        
    #resets snake when dead   
    
    #TODO ADD A DEATH BY MESSAGE TO SEE WHY THE SNAKE DIES RANDOMLY
    def die(self):
        for i in range(len(self.snake_body[2:])):
             if self.snake_head.colliderect(self.snake_body[i]):
               self.dead = True
               print("DEATH BY SELF")
               break
               
       
                
        if self.snake_head.bottom >= 600 + self.size or self.snake_head.top <=0 - self.size :
            print("death by wall on the y axis")
            self.dead = True           
            
            
        if self.snake_head.right >= 800 + self.size or self.snake_head.left <= 0 - self.size:
            print("death by wall on the x axis")
            self.dead = True
            
            
        
        return self.dead
    
    #resets snake 
    def reset(self):
        self.snake_body = [pygame.Rect(800/2 - self.block_size,600/2 ,self.size,self.size)]
        self.snake_head = (pygame.Rect(800/2,600/2,self.size,self.size))
        self.xdirection = 0
        self.ydirection = 0
        self.dead = False
        



    