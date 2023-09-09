import pygame
from pygame.locals import *
import Constants

class Enemy:
	def __init__(self, pos, size, spd):

		self.pos = pos
		self.size = size
		self.spd = spd
		self.vel = pygame.Vector2(0,0)
		self.color = Constants.ENEMY_COLOR
		self.center = self.calcCenter()

	def __str__(self):
		return ("Size: " +  str(self.size) + ", " + "Pos: " + str(self.pos) + ", " + "Vel: " + str(self.vel) + ", " + "Center: " + str(self.center))

	def draw(self, screen):

		#draw the rectangle
		pygame.draw.rect(screen, (Constants.ENEMY_COLOR), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

		# draw debug line
		lineStart = self.calcCenter()
		scaledVel = pygame.Vector2(self.vel.x, self.vel.y)
		
		if self.vel == (0,0):
			scaledVel = self.vel
		else:
			pygame.Vector2.scale_to_length(scaledVel, self.size)
		
		lineEnd = pygame.Vector2(self.calcCenter().x + scaledVel.x, self.calcCenter().y + scaledVel.y)
		pygame.draw.line(screen, (0, 0, 255), lineStart, lineEnd, 3)

	def update(self, player):

		# flee if player is close enough
		distance = self.pos - player.pos
		if distance.length() < Constants.FLEE_RANGE:
			self.vel = pygame.Vector2.normalize(distance)
			#Use speed and multiply it by velocity and time in order to determine where the enemy should move

		# otherwise, wander
		print("Wander...")

	def calcCenter(self):
		return pygame.Vector2(self.pos.x + self.size / 2, self.pos.y + self.size / 2)