import pygame
from pygame.locals import *
import random
import math
import Constants
from Agent import Agent

class Enemy(Agent):
	
	def update(self, player):
		
		# flee if player is close enough
		distance = self.pos - player.pos
		if distance.length() < Constants.FLEE_RANGE:
			self.vel = pygame.Vector2.normalize(distance) * Constants.ENEMY_SPD
			self.pos += self.vel

		# otherwise, wander
		else:
			rotationAngle = random.randrange(-1, 1)
			theta = math.acos(rotationAngle)

			pickTurn = random.randint(0, 100)
			if pickTurn < 50:
				pass
			else:
				theta += 180

			self.vel.x += math.cos(theta) - math.sin(theta)
			self.vel.y += math.sin(theta) - math.cos(theta)

			self.pos += pygame.Vector2.normalize(self.vel)