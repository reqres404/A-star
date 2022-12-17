import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A Star Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# TO MAKE THE GRID AND VISULAIZE THE PATH FINDING PROCESS
class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row*width #To Color the cubes on the grid
        self.y = col*width #To Color the cubes on the grid
        self.color = WHITE
        self.nieghbors = []
        self.total_rows = total_rows
    
    # Just Gives The Position of cubes so we can use it in Further Code
    def get_pos(self):
        return self.row,self.col
    
    # Give the Positon for the cubes That are to be turned red as there's no furhter Paths
    def is_closed(self):
        return self.color == RED;
    
    # Gives The cubes where barrier don't exists
    def is_open(self):
        return self.color == GREEN;

    #Functions to make barriers
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
            
    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        return self.color == WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE
        
    
