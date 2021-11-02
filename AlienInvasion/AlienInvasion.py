import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien
from scoreboard import Scoreboard
from button import Button


from game_stats import GameStats

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
		
		#Create an instance to store game_stats
		self.stats = GameStats(self)
		#create an instance to store game statistics and score_board
		self.sb = Scoreboard(self)
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		
		#make a play button
		self.play_button = Button(self,"Play")
		
	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_aliens()
				self._update_bullets()
				
			self._update_screen()
			
			

	#These methods are for fleet directions and adges
	
	def _check_fleet_edges(self):
		"""respond approprietly if any alien reaches edges"""
		for alien in self.aliens.sprites():
			if alien._check_edges():
				self._change_fleet_direction()
				break
				
	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1
	
	def _update_bullets(self):
		"""Update the possition of bullets and get rid of the old bullets"""
		#Update the bullet positions 
		self.bullets.update()
		
		#Get rid of the bullets that have disapeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)
		
		self._check_alien_bullet_collision()
		
		
				
	def _check_alien_bullet_collision(self):
		"""Respond to bullect alien collision"""
		#Remove any bullets or alien that have collided
		#Check if the bullets that have hit the aliens 
		#if so, get rid of the bullet and the alien 
		collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
		
		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points *len(aliens)
			self.sb.prep_score()
			self.sb.check_high_scores()
			
			#Increas ethe level
			self.stats.level += 1
			self.sb.prepare_level()
			
		
		if not self.aliens:
			#Destroy the existing bullets and create a new fleet 
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()
				
	def _check_events(self):
		#this methods is for events and mouse movements 
		for even in pygame.event.get():
			if even.type == pygame.QUIT:
				sys.exit()
			elif even.type == pygame.KEYDOWN:
				self._check_keyDown_events(even)
											
			elif even.type == pygame.KEYUP:
				self._check_keyUp_events(even)
			elif even.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
				
	def _check_play_button(self,mouse_pos):
		"""Start a new game when a player clicks play."""
		button_clicked =  self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			#reset to the initial_values 
			self.settings.initialize_dynamic_settings()
			#reset the game statistics
			self.stats.reset_stats()
			self.stats.game_active = True 
			self.sb.prep_score()
			
			#This below is the method to update the level
			self.sb.prepare_level()
			
			#This bellow is a function to update and show ships remaining
			self.sb.prep_ships()
			
			#Get rid of any remaining alliens and bullets 
			self.aliens.empty()
			self.bullets.empty()
			
			#Create a new fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()
			
			#Hide the mouse cursor
			pygame.mouse.set_visible(False)
				
	def _update_aliens(self):
	
		"""
		Check if the fleet is at the edge;
		and update the positions of all aliens in the fleet
		"""
		self._check_fleet_edges()
		"""update the positions of all the aliens in the fleet """
		self.aliens.update()
		
		#look for alien ship collisions
		
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()
			
		#Look for aliens hitting te bottom of the screen 
		self._check_aliens_bottom()
			
	def _ship_hit(self):
		"""Respond to ship being hit by the aliens"""
		if self.stats.ship_left > 0:
			#Decrement ships left and display the remaining 
			self.stats.ship_left -=1
			
			self.sb.prep_ships()
			
			#Get rid of any remaing aliens and bullets
			self.aliens.empty()
			self.bullets.empty()
			
			#Create new aliens and center the ship
			self._create_fleet()
			self.ship.center_ship()
			
			#pause
			sleep(0.5)
		else:
			self.stats.game_active = False
			#Make the cursor seen again
			pygame.mouse.set_visible(True)
	
	def _check_aliens_bottom(self):
		"""Check if the aliens have reached the ground or bottom of the screen"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >=screen_rect.bottom:
				#Treat this the same way as when the ship got hit
				self._ship_hit()
				break
		
	
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
		
		# Draw a score information 
		self.sb.show_score()

		
		#Draw the button if the game is inactive 
		if not self.stats.game_active:
			self.play_button.draw_button()
			
		#Make the most recently drawn screen visible
		pygame.display.flip()
		
		
	def _create_fleet(self):
		"""Create the first row  of aliens"""
		#create aliens 
		#Create an alien and find the number of aliens in a row 
		#Spacing between each alien is equal to one alien width
		alien = Alien(self)
		#self.aliens.add(alien)
		alien_width,alien_height = alien.rect.size
		
		available_space_x = self.settings.screen_width - (2* alien_width)
		number_aliens_x = available_space_x//(2 * alien_width)
		
		"""Determine the  number of rows of aliens that fit on the screen"""
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		
		number_rows = available_space_y //(2 * alien_height)
		
		#create a full fleet of aliens
		for number_row in range(number_rows):
			#Create the first row of aliens
			for alien_number in range(number_aliens_x):
				"""Create an alien and place it in a row """
				self._create_Alien(alien_number,number_row)
	
	def _create_Alien(self,alien_number,number_row):
		"""create alien and place it in a row"""
		alien = Alien(self)
		alien_width,alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_row
		self.aliens.add(alien)
		
		

if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
