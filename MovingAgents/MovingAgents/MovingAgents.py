import pygame
from pygame.locals import *
import Constants
from Player import Player

#initialize pygame
pygame.init()

#setup
yPos = Constants.DISPLAY_HEIGHT / 2
xPos = Constants.DISPLAY_WIDTH / 2
clock = pygame.time.Clock();
screen = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
player = Player(pygame.Vector2(xPos, yPos), (Constants.PLAYER_SIZE), Constants.PLAYER_SPD)

#main gameplay loop
while True:

	enemies = []

	#draw the player
	player.draw(screen)

	#update the player
	player.update(enemies)
