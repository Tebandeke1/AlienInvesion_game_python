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
		self.settings = ai_game.settings
		
		
		#Load the ship image and get the ship rect.
		self.image = pygame.image.load('images/shi.bmp')
		self.rect = self.image.get_rect()
		
		#store the decimal value for the ships horizontal position
		self.x = float(self.rect.x)
		
		#Start each new ship at the bottom center of the screen 
		self.rect.midbottom = self.screen_rect.midbottom
		
	def update(self):
		#update the ship position based on the movement flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
			
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		
		#Update rect object from self.x
		self.rect.x = self.x
			
	def blitme(self):
		"""Draw the ship at it's current location.""" 
		self.screen.blit(self.image,self.rect)
