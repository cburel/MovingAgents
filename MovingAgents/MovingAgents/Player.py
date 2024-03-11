from typing import List
import pygame
from pygame.locals import *
from Agent import Agent

#setup
clock = pygame.time.Clock();


class Player(Agent):

	def update(self, enemies: List):

		# gets nearest enemy and moves player towards it
		enemy = None

		if len(enemies) != 0:
			enemy = min([e for e in enemies], key=lambda e: self.pos.distance_to(pygame.math.Vector2(e.pos.x, e.pos.y)))

			self.vel = enemy.pos - self.pos
				
			super().update(enemy)

		return enemy