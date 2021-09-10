import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	"""This is Alien class for placing an alien image on the screen"""
	
	def __init__(self,ai_game):
		"""Here were initialising the alien ship and setting the starting position"""
		super(Alien,self).__init__()
		self.screen = ai_game.screen
		
		"""load the alien image and set its rect position"""
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()
		
		#start each new alien near the topleft of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the aliens exact horizontal position 
		self.x = float(self.rect.x)
	
