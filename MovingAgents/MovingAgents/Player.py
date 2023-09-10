from typing import List, Self
import pygame
from pygame.locals import *
import Constants
import random
import Agent

#setup
clock = pygame.time.Clock();


class Player(Agent):

	def __init__(self, pos, size, spd):
		self.pos = pos
		self.size = size
		self.spd = spd
		self.vel = pygame.Vector2(0,0)
		self.center = self.calcCenter()

	def __str__(self):
		return ("Size: " +  str(self.size) + ", " + "Pos: " + str(self.pos) + ", " + "Vel: " + str(self.vel) + ", " + "Center: " + str(self.center))

	def draw(self, screen):

		#draw the rectangle
		pygame.draw.rect(screen, (Constants.PLAYER_COLOR), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

		# draw debug line
		lineStart = self.calcCenter()
		scaledVel = pygame.Vector2(self.vel.x, self.vel.y)
		
		if self.vel == (0,0):
			scaledVel = self.vel
		else:
			pygame.Vector2.scale_to_length(scaledVel, self.size)
		
		lineEnd = pygame.Vector2(self.calcCenter().x + scaledVel.x, self.calcCenter().y + scaledVel.y)
		pygame.draw.line(screen, (0, 0, 255), lineStart, lineEnd, 3)

	def update(self, enemies: List):

		# gets nearest enemy and moves player towards it
		# shoutout to Rabbid76 on SO for the basics on this next line
		enemy = min([e for e in enemies], key=lambda e: self.pos.distance_to(pygame.math.Vector2(e.pos.x, e.pos.y)))
		self.vel = enemy.pos - self.pos
				
		self.vel = pygame.Vector2.normalize(self.vel)
		self.pos += self.vel

	def calcCenter(self):
		return pygame.Vector2(self.pos.x + self.size / 2, self.pos.y + self.size / 2)