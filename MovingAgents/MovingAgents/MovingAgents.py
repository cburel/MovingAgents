import pygame
from pygame.locals import *
import Constants
from Player import Player

#initialize pygame
pygame.init()

#setup
clock = pygame.time.Clock();
screen = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
player = Player(pygame.Vector2(Constants.PLAYER_XPOS, Constants.PLAYER_YPOS), (Constants.PLAYER_SIZE), Constants.PLAYER_SPD)

#main gameplay loop
while True:
		
	enemies = []

	# event handler
	for event in pygame.event.get():

		#quit the game
		if event.type == QUIT:
			pygame.quit()
			quit()

	#draw the player
	player.draw(screen)

	#update the player
	player.update(enemies)

	#flip display buffer
	pygame.display.flip()

	#constrain to 60 fps
	clock.tick(60)
