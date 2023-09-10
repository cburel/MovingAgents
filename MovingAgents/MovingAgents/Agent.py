import pygame
from pygame.locals import *
import Constants
import random
import math

class Agent():
	def __init__(self, pos, size, spd, color):
		self.pos = pos
		self.size = size
		self.spd = spd
		self.color = color
		self.vel = pygame.Vector2(0,0)
		self.center = self.calcCenter()
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)

	#pretty print agent information
	def __str__(self):
		return ("Size: " +  str(self.size) + ", " + "Pos: " + str(self.pos) + ", " + "Vel: " + str(self.vel) + ", " + "Center: " + str(self.center))

	def draw(self, screen):

		#draw the rectangle
		pygame.draw.rect(screen, self.color, pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)
		
		#debug
		#pygame.draw.rect(screen, (255,255,255), self.rect)

		# draw debug line
		lineStart = self.calcCenter()
		scaledVel = pygame.Vector2(self.vel.x, self.vel.y)
		
		if self.vel == (0,0):
			scaledVel = self.vel
		else:
			pygame.Vector2.scale_to_length(scaledVel, self.size)
		
		lineEnd = pygame.Vector2(self.calcCenter().x + scaledVel.x, self.calcCenter().y + scaledVel.y)
		pygame.draw.line(screen, (0, 0, 255), lineStart, lineEnd, 3)

		#draw target line
		#pygame.draw.line(screen, (255, 0, 0), (self.calcCenter().x, self.calcCenter().y), (other.calcCenter().x, other.calcCenter.y), 3)
	
	# check for collision with another agent
	def detectCollision(self, other):

		# if collision is detected, execute collision 
		if self.rect.colliderect(other.rect):
			self.tagged()

	def update(self):

		#move the agent and its collision rect
		self.pos += pygame.Vector2.normalize(self.vel) * self.spd
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)

		#keep agent in bounds of world and make them move off borders a little nicer
		if self.pos.x <= 0:
			self.pos.x = Constants.BORDER_RADIUS + self.size
			self.vel.x = -self.vel.x
		if self.pos.x >= Constants.DISPLAY_WIDTH:
			self.pos.x = Constants.DISPLAY_WIDTH - Constants.BORDER_RADIUS - self.size
			self.vel.x = -self.vel.x
		if self.pos.y <= 0:
			self.pos.y = Constants.BORDER_RADIUS + self.size
			self.vel.y = -self.vel.y
		if self.pos.y >= Constants.DISPLAY_HEIGHT:
			self.pos.y = Constants.DISPLAY_HEIGHT - Constants.BORDER_RADIUS - self.size
			self.vel.y = -self.vel.y

	# calculate the center of the agent's rect
	def calcCenter(self):
		return pygame.Vector2(self.pos.x + self.size / 2, self.pos.y + self.size / 2)


			