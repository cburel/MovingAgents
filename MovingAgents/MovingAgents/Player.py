from typing import List, Self
import pygame
from pygame.locals import *
import Constants
import random
from Agent import Agent

#setup
clock = pygame.time.Clock();


class Player(Agent):

	def update(self, enemies: List):

		# gets nearest enemy and moves player towards it
		# shoutout to Rabbid76 on SO for the basics on this next line
		enemy = min([e for e in enemies], key=lambda e: self.pos.distance_to(pygame.math.Vector2(e.pos.x, e.pos.y)))
		self.vel = enemy.pos - self.pos
				
		self.vel = pygame.Vector2.normalize(self.vel)
		self.pos += self.vel