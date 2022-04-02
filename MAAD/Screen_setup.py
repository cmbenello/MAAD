import pygame, sys

#General setup
pygame.init() # need for all pygame code
clock = pygame.time.Clock()


# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))#Create the Screen
pygame.display.set_caption('Pongation')


#ball - (Center - ball size / 2) xtx make function to generate 
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

while True:
	#Handling inputs
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #checks if user has pressed exit button
			pygame.quit()
			sys.exit()
	
	#Moves the ball every single cycle
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	#to reflect the ball just multiple the speed by -1


	# if ball.colliderect(maze) do collision

	#Visuals
	screen.fill(bg_color) #Draw the screen color first 
	#xtx insert the maze as a regular surface
	pygame.draw.ellipse(screen, light_grey, ball) #Then draw the ball


	# Updating the window 
	pygame.display.flip() #Draws the picture
	clock.tick(60) #Limits how fast the loop runs

pygame.quit()