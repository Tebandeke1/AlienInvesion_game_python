import pygame.font

from pygame.sprite import Group
from ship import Ship

class Scoreboard:
	"""A class show the scores on the screen """
	
	def __init__(self ,ai_game):
		"""Initialize score keeping attributes"""
		
		self.screen = ai_game.screen
		
		self.ai_game = ai_game
		
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		
		#font for scoring information 
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		
		#Prepare the initial score image 
		self.prep_score()
		self.prepare_high_score()
		self.prepare_level()
		
		self.prep_ships()
		
	def prep_ships(self):
		"""Show how many ships are remaining"""
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def prepare_level(self):
		"""Turn the level into the rendered image"""
		level = str(self.stats.level)
		self.game_level = self.font.render(level,True,self.text_color,self.settings.bg_color)
		#Position the level below the score 
		
		self.level_rect = self.game_level.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom+10
		
	def prepare_high_score(self):
		"""Turn the high score into the rendered image"""
		#Rounding the score from here
		high_score = round(self.stats.high_score)
		high_score_str = "{:,}".format(self.stats.high_score)
		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
		
		#Center the high score at the top of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
		
	def prep_score(self):
		"""Turn the score into a rendered image"""
		
		#Rounding the scores here
		rounded_score = round(self.stats.score)
		score_str = "{:,}".format(self.stats.score)
		self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)
		
		# Displa the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def show_score(self):
		"""Draw score, level and ships on the screen"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.game_level,self.level_rect)
		self.ships.draw(self.screen)
		
	def check_high_scores(self):
		"""Check to see if there is a new high score"""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prepare_high_score()
		
		
