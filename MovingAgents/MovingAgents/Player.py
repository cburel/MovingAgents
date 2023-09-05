from typing import List
import pygame


class Player:

	def __init__(self, pos, size, spd):
		self.pos = pos
		self.size = size
		self.spd = spd
		vel = 0
		center = self.calcCenter()

	def __str__(self):
		return ("Size: " +  str(self.size) + ", " + "Pos: " + str(self.pos) + ", " + "Vel: " + str(self.vel) + ", " + "Center: " + str(self.center))

	def draw(self, screen):
		#draw the rectangle
		pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

		# draw debug line
		lineStartX = self.pos.x + self.size/2
		lineStartY = self.pos.y + self.size/2
		scaledVel = pygame.Vector2.scale(self.vel, self.size)
		lineEndX = (self.pos.x + self.size/2) + scaledVel.x
		lineEndY = (self.pos.y + self.size/2) + scaledVel.y
		pygame.draw.line(screen, (0, 0, 255), (lineStartX, lineStartY), (lineEndX, lineEndY), 3)

	def update(self, enemies: List):
		pass

	def calcCenter(self):
		pass