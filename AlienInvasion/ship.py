import pygame

class Ship:
	"""A class to manage the ship"""
	
	def __init__(self,ai_game):
		"""Initialize the ship and get it's starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		#movement flag
		self.moving_right = False
		self.moving_left = False
		
		#Load the ship image and get the ship rect.
		self.image = pygame.image.load('images/shi.bmp')
		self.rect = self.image.get_rect()
		
		#Start each new ship at the bottom center of the screen 
		self.rect.midbottom = self.screen_rect.midbottom
		
	def update(self):
		#update the ship position based on the movement flag
		if self.moving_right:
			self.rect.x += 1
			
		if self.moving_left:
			self.rect.x -=1
			
	def blitme(self):
		"""Draw the ship at it's current location.""" 
		self.screen.blit(self.image,self.rect)
