from typing import List, Self
import pygame
from pygame.locals import *
import Constants

#setup
clock = pygame.time.Clock();


class Player:

	def __init__(self, pos, size, spd):
		self.pos = pos
		self.size = size
		self.spd = spd
		self.vel = pygame.Vector2(0,0)
		self.center = self.calcCenter()

	def __str__(self):
		return ("Size: " +  str(self.size) + ", " + "Pos: " + str(self.pos) + ", " + "Vel: " + str(self.vel) + ", " + "Center: " + str(self.center))

	def draw(self, screen):
		
		#make screen cornflower blue
		screen.fill(Constants.BACKGROUND_COLOR)

		#draw the rectangle
		pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

		# draw debug line
		lineStart = self.calcCenter()
		scaledVel = pygame.Vector2(self.vel.x, self.vel.y)
		
		if self.vel == (0,0):
			scaledVel = self.vel
		else:
			pygame.Vector2.scale_to_length(scaledVel, self.size)
		
		lineEnd = pygame.Vector2(self.calcCenter().x + scaledVel.x, self.calcCenter().y + scaledVel.y)
		pygame.draw.line(screen, (0, 0, 255), lineStart, lineEnd, 3)

		
		#flip display buffer
		pygame.display.flip()

		#constrain to set fps
		clock.tick(Constants.FRAME_RATE)

	def update(self, enemies: List):
		
		
		keyPressed = pygame.key.get_pressed()

		# event handler
		for event in pygame.event.get():

			#quit the game
			if event.type == QUIT:
				pygame.quit()
				quit()

			#movement
			if any(keyPressed):
				
				if keyPressed[pygame.K_w]: #move up
					self.vel -= pygame.Vector2(0, Constants.PLAYER_SPD)
				if keyPressed[pygame.K_s]: #move down
					self.vel += pygame.Vector2(0, Constants.PLAYER_SPD)
				if keyPressed[pygame.K_a]: #move left
					self.vel -= pygame.Vector2(Constants.PLAYER_SPD, 0)
				if keyPressed[pygame.K_d]: #move right
					self.vel += pygame.Vector2(Constants.PLAYER_SPD, 0)
				
				self.vel = pygame.Vector2.normalize(self.vel)
				self.pos += self.vel

			#flip display buffer
			pygame.display.flip()

			#constrain to 60 fps
			clock.tick(60)

	def calcCenter(self):
		return pygame.Vector2(self.pos.x + self.size / 2, self.pos.y + self.size / 2)