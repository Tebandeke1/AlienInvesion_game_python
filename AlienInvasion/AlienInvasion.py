import sys
import pygame
from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien
class AlienInvasion:
	"""Overall class to mange assets and behaviior"""
	def __init__(self):
		"""Initializing the game, and create game resources"""
		pygame.init()
		self.settings = Settings()
		
		# These are for FULL_SCREEN mode 
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		#self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		
		
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		
	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
			
			
	
	def _update_bullets(self):
		"""Update the possition of bullets and get rid of the old bullets"""
		#Update the bullet positions 
		self.bullets.update()
		
		#Get rid of the bullets that have disapeared			
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)
		
				
				
	def _check_events(self):
		#this methods is for events and mouse movements 
		for even in pygame.event.get():
			if even.type == pygame.QUIT:
				sys.exit()
			elif even.type == pygame.KEYDOWN:
				self._check_keyDown_events(even)
											
			elif even.type == pygame.KEYUP:
				self._check_keyUp_events(even)
				
					
	def _check_keyDown_events(self,even):
		# Respond to key Presses
		if even.key == pygame.K_RIGHT:
			#move the ship to the right every time the right key is pressed
			self.ship.moving_right = True	
		elif even.key == pygame.K_LEFT:
			#moving the ship to the left every time the left key is pressed
			self.ship.moving_left = True
		elif even.key == pygame.K_q:
			sys.exit()
		elif even.key == pygame.K_SPACE:
			self._fire_bullets()
			
	def _fire_bullets(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullets(self)
			self.bullets.add(new_bullet)
			
	def _check_keyUp_events(self,even):
		# Respond to key Releases
		if even.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif even.key == pygame.K_LEFT:
			self.ship.moving_left = False
		
					
	def _update_screen(self):		
		#Redraw the screen using each path trough the loop
		self.screen.fill(self.settings.bg_color)
		
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		#here were making the alien appear on the screen 
		self.aliens.draw(self.screen)

		#Make the most recently drawn screen visible
		pygame.display.flip()
		
		
	def _create_fleet(self):
		"""Create a fleet of aliens"""
		#create aliens 
		#Create an alien and find the number of aliens in a row 
		#Spacing between each alien is equal to one alien width
		alien = Alien(self)
		#self.aliens.add(alien)
		alien_width = alien.rect.width
		
		available_space_x = self.settings.screen_width - (2* alien_width)
		number_aliens_x = available_space_x//(2 * alien_width)
		
		#Create the first row of aliens
		for alien_number in range(number_aliens_x):
			"""Create an alien and place it in a row """
			alien = Alien(self)
			alien.x = alien_width + 2 * alien_width * alien_number
			alien.rect.x = alien.x
			self.aliens.add(alien)
			
		
		

if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
