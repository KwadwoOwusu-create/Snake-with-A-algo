import pygame,sys
from snake import snake
from food import food
from grid import grid
from pause import pause

pygame.init()

#displays for the screen
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width , display_height))
title = "snake"
pygame.display.set_caption(title)

#ticks
clock = pygame.time.Clock()

#event habndiling
event = pygame.USEREVENT + 1

#other classes
grid = grid()
snake = snake(grid.block_size)
food = food(display_height,display_width,grid.block_size)

#points
point_num = 0

#font 
font = pygame.font.Font("04B_30__.ttf", 100)
point= font.render(str(point_num), True, (184,111,82))
point1= font.render(str(point_num), True, "black")

pause = pause(screen)

    

#game loop
while pause.checker:
    if snake.die():
        break
    
    #if you click the x it quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            #if w is pressed player1 moves up, or if the up arrow is pressed player 2 moves up
            if event.key == pygame.K_SPACE:
                pause.checker = False
                pause.run()
            elif event.key == pygame.K_SPACE and pause.checker == False:
                pause.checker = True 
        
    #fill every frame 
    screen.fill((250,212,216))
    
    #draw screen grid 
    grid.draw_grid(100,25,screen)
    
    #render points 
    screen.blit(point1,(800/2 + 8 ,0 + 6))
    screen.blit(point,(800/2 ,0))
    
    
    
    #snake stuff
    snake.draw_body(screen)
    snake.draw_head(screen)
    snake.update()
    #snake.handle_keys()
    
    snake.ai_snake(food.food.x,food.food.y)
    
    
    #food stuff
    food.draw(screen)
    
    #collision between food and snake 
    if food.collide(snake.snake_head) == True:
        #increase points
        point_num+=1
        #re render points
        point= font.render(str(point_num), True, (184,111,82))
        point1= font.render(str(point_num), True, "black")
        #make snake bigger
        snake.grow()
        #change the food position
        food.position()
    
    #kills snake if hits the edges or collides with self
    
    
    #resets everything 
    if snake.die() == True:
        print(point_num)
        point_num = 0
        point= font.render(str(point_num), True, (184,111,82))
        point1= font.render(str(point_num), True, "black")
        food.eaten = True
        food.position()
        snake.reset()
        
    
    #updates the display according with the screen fill
    pygame.display.update()
    
    

    #runs the game at 10 fps 
    clock.tick(10)
    