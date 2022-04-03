import random
import pygame
import math
pygame.init()

#Create some common colors
WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)


#Set up the Screen
size = (800,800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pongation")

done = False

clock = pygame.time.Clock()

width = 100
cols = int(size[0] / width)
rows = int(size[1] / width)


girth = 2 #Thickness of the llines
walls_list = []

stack = []

#Intialise some information about the balls

ball_size = width/5
ball_list = [] # A list of all the balls in the form, [ball, speed_x, speed_y]
ball_speed = 4
number_of_balls = 5

for i in range(1,number_of_balls): #A simple thing is just to shoot each ball at a degree
    ball_i = pygame.Rect(ball_size / 2,ball_size / 2, ball_size, ball_size)
    ball_list.append([ball_i, 
        ball_speed * math.cos(i * (180 / number_of_balls) * math.pi / 180), 
        ball_speed * math.sin(i * (180 / number_of_balls) * math.pi / 180) ])

def ball_movement():
    global ball_list,grid
    for pos,i in enumerate(ball_list):
        ball = i[0]
        speed_x = i[1]
        speed_y = i[2]
        ball.x += speed_x
        ball.y += speed_y
        if ball.top <= 0 or ball.bottom >= size[1]:
            ball_list[pos][2] *= -1
        if ball.left <= 0 or ball.right >= size[0]:
            ball_list[pos][1] *= -1

        #This technique is wrong becuase you could intersect 
        if ball.collidelist(walls_list) != -1:
            if abs (ball.x % width) == 0:
                ball_list[pos][1] *= -1
            if abs (ball.y % width) == 0:
                ball_list[pos][1] *= -1


class Cell():
    def __init__(self,x,y):
        global width
        self.x = x * width
        self.y = y * width
        
        self.visited = False
        self.current = False
        
        self.walls = [True,True,True,True] # top , right , bottom , left
        
        # neighbors
        self.neighbors = []
        
        self.top = 0
        self.right = 0
        self.bottom = 0
        self.left = 0
        
        self.next_cell = 0
    
    def draw(self):
        '''if self.current:
            pygame.draw.rect(screen,RED,(self.x,self.y,width,width))'''
        if self.walls[0]:
            pygame.draw.line(screen,WHITE,(self.x,self.y),((self.x + width),self.y),5) # top
        if self.walls[1]:
            pygame.draw.line(screen,WHITE,((self.x + width),self.y),((self.x + width),(self.y + width)),5) # right
        if self.walls[2]:
            pygame.draw.line(screen,WHITE,((self.x + width),(self.y + width)),(self.x,(self.y + width)),5) # bottom
        if self.walls[3]:
            pygame.draw.line(screen,WHITE,(self.x,(self.y + width)),(self.x,self.y),5) # left
    
    def rect_list(self):
        global walls_list
        if self.walls[0]:
            walls_list.append(pygame.Rect(self.x, self.y,width,girth)) #top
        #if self.walls[1]:
         #   walls_list.append(pygame.Rect(self.x + width, self.y, girth, width)) #right
        #if self.walls[2]:
            #walls_list.append(pygame.Rect(self.x, self.y -  width, width, girth)) #bottom
        if self.walls[3]:
            walls_list.append(pygame.Rect(self.x,self.y, girth, width)) #left
    
    def checkNeighbors(self):
        if int(self.y / width) - 1 >= 0:
            self.top = grid[int(self.y / width) - 1][int(self.x / width)]
        if int(self.x / width) + 1 <= cols - 1:
            self.right = grid[int(self.y / width)][int(self.x / width) + 1]
        if int(self.y / width) + 1 <= rows - 1:
            self.bottom = grid[int(self.y / width) + 1][int(self.x / width)]
        if int(self.x / width) - 1 >= 0:
            self.left = grid[int(self.y / width)][int(self.x / width) - 1]
        
        if self.top != 0:
            if self.top.visited == False:
                self.neighbors.append(self.top)
        if self.right != 0:
            if self.right.visited == False:
                self.neighbors.append(self.right)
        if self.bottom != 0:
            if self.bottom.visited == False:
                self.neighbors.append(self.bottom)
        if self.left != 0:
            if self.left.visited == False:
                self.neighbors.append(self.left)
        
        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.next_cell
        else:
            return False

def removeWalls(current_cell,next_cell):
    x = int(current_cell.x / width) - int(next_cell.x / width)
    y = int(current_cell.y / width) - int(next_cell.y / width)
    if x == -1: # right of current
        current_cell.walls[1] = False
        next_cell.walls[3] = False
    elif x == 1: # left of current
        current_cell.walls[3] = False
        next_cell.walls[1] = False
    elif y == -1: # bottom of current
        current_cell.walls[2] = False
        next_cell.walls[0] = False
    elif y == 1: # top of current
        current_cell.walls[0] = False
        next_cell.walls[2] = False


grid = []

for y in range(rows):
    grid.append([])
    for x in range(cols):
        grid[y].append(Cell(x,y))

current_cell = grid[0][0]
next_cell = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    current_cell.visited = True
    current_cell.current = True
    

    
    next_cell = current_cell.checkNeighbors()
    screen.fill(BLACK)
    if next_cell != False:
        current_cell.neighbors = []
        
        stack.append(current_cell)
        
        removeWalls(current_cell,next_cell)
        
        current_cell.current = False
        
        current_cell = next_cell
    
    elif len(stack) > 0:
        current_cell.current = False
        current_cell = stack.pop()
    

    
    elif len(stack) == 0: #Finished creating the maze
        for y in range(rows):
            for x in range(cols):
                grid[y][x].draw()
                grid[y][x].rect_list()
        for i in walls_list:
            pygame.draw.rect(screen, RED, i )

        ball_movement()
        for ball in ball_list:
            pygame.draw.ellipse(screen, WHITE, ball[0])
        #xtx create function that navigates the ball

    pygame.display.flip()
    
    clock.tick(1000)


pygame.quit()