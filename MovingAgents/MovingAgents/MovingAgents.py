import pygame
from pygame.locals import *
import Constants
import random
from Enemy import Enemy
from Player import Player

#initialize pygame
pygame.init()

#setup
clock = pygame.time.Clock();
screen = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
player = Player(pygame.Vector2(Constants.PLAYER_XPOS, Constants.PLAYER_YPOS), (Constants.PLAYER_SIZE), Constants.PLAYER_SPD, Constants.PLAYER_COLOR)

enemies = []
for i in range (1, Constants.MAX_ENEMIES + 1):
	enemies.append(Enemy(pygame.Vector2(random.randrange(0, Constants.DISPLAY_WIDTH), random.randrange(0, Constants.DISPLAY_WIDTH)), Constants.ENEMY_SIZE, Constants.ENEMY_SPD, Constants.ENEMY_COLOR))

#main gameplay loop
while True:

	# event handler
	for event in pygame.event.get():

		#quit the game
		if event.type == QUIT:
			pygame.quit()
			quit()
				
	#make screen cornflower blue
	screen.fill(Constants.BACKGROUND_COLOR)
	
	#update the agents
	player.update(enemies)
	for enemy in enemies:
		enemy.update(player)

	#draw the agents
	player.draw(screen)
	for enemy in enemies:
		enemy.draw(screen)

	# check for player tagging enemy
	player.detectCollision(enemy)

	#flip display buffer
	pygame.display.flip()

	#constrain to 60 fps
	clock.tick(60)
