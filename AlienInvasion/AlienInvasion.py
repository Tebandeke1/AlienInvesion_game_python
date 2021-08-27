import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to mange assets and behaviior"""
	def __init__(self):
		"""Initializing the game, and create game resources"""
		pygame.init()
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		
	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()
				
				
	def _check_events(self):
		#this methods is for events and mouse movements 
		for even in pygame.event.get():
			if even.type == pygame.QUIT:
				sys.exit()
			elif even.type == pygame.KEYDOWN:
				if even.key == pygame.K_RIGHT:
					#move the ship to the rigth every time the right key is pressed
					self.ship.moving_right = True	
				if even.key == pygame.K_LEFT:
					#moving the ship to the left every time the left key is pressed
					self.ship.moving_left = True
										
			elif even.type == pygame.KEYUP:
				if even.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				if even.key == pygame.K_LEFT:
					self.ship.moving_left = False
					
	def _update_screen(self):		
		#Redraw the screen using each path trough the  loop
		self.screen.fill(self.settings.bg_color)
		
		self.ship.blitme()

		#Mamke the most recently drawn screen visible
		pygame.display.flip()

if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
