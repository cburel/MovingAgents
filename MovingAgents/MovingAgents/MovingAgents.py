import pygame
from pygame.locals import *
import Constants
from Player import Player

#initialize pygame
pygame.init()

#setup
yPos = 30
xPos = 30
initVel = 0
clock = pygame.time.Clock();
screen = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
player = Player(pygame.Vector2(xPos, yPos), pygame.Vector2(initVel, initVel), (Constants.PLAYER_SIZE))

#main gameplay loop
while True:

	player.draw(screen)

	# event handler
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()

	#make screen cornflower blue
	screen.fill(Constants.BACKGROUND_COLOR)

	#flip display buffer
	pygame.display.flip()

	#constrain to set fps
	clock.tick(Constants.FRAME_RATE)
