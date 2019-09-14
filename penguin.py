import pygame

class Penguin():

	def __init__(self, screen):
		"""Initiliaze the Penguin and the screen"""
		self.screen = screen

		#Load the ship image and get its rect.

		self.image = pygame.image.load('images/penguin1.bmp') #importing the image
		self.rect = self.image.get_rect()	#rect == game object's position/coords
		self.screen_rect = screen.get_rect()	#this is the entire screen's coords

		#Start each new ship at the center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		"""Draw the ship at its current location."""
		#draws onto screen arg1 with coords arg2
		self.screen.blit(self.image, self.rect) 