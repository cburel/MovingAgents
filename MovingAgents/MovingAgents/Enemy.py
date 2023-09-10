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
			self.vel = pygame.Vector2.normalize(distance)

		# otherwise, wander
		else:
			rotationAngle = random.randrange(-1, 1)
			theta = math.acos(rotationAngle)

			pickTurn = random.randint(0, 100)
			if pickTurn < 50:
				theta += 0
			else:
				theta += 180

			self.vel.x += math.cos(theta) - math.sin(theta)
			self.vel.y += math.sin(theta) - math.cos(theta)

		super().update()

	def tagged(self):
		self.color = (0,0,0)
		self.size = (0,0)
		print("enemy collision!")