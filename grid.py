import pygame

class grid: 
    def __init__(self) -> None:
        self.block_size = 25
        self.color = None
   
    #draw grid based on the block sze
    def draw_grid(self, grid_size, square_size, screen):
        for i in range(grid_size):
            for j in range(grid_size):
                # Determine the color based on the sum of the row and column indices
                if(i+j) % 2 == 0:
                    self.color = (80, 63, 68)
                else:
                    self.color = (85, 67, 72)

                # Draw the square
                pygame.draw.rect(screen, self.color, [square_size * i, square_size * j, square_size, square_size])