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
		
		self.settings = ai_game.settings
		
		#store the aliens exact horizontal position 
		self.x = float(self.rect.x)
		
	def _check_edges(self):
		"""return true if the ship is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <=0:
			return True
		
	def update(self):
		"""move the aliens to the right or left"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x
	
