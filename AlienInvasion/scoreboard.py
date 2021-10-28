import pygame.font

class Scoreboard:
	"""A class show the scores on the screen """
	
	def __init__(self ,ai_game):
		"""Initialize score keeping attributes"""
		
		self.screen = ai_game.screen
		
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		
		#font for scoring information 
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		
		#Prepare the initial score image 
		self.prep_score()
	def prep_score(self):
		"""Turn the score into a rendered image"""
		
		#Rounding the scores here
		rounded_score = round(self.stats.score)
		score_str = "{:,}".format(self.stats.score)
		self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)
		
		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def show_score(self):
		"""Draw score on the screen"""
		self.screen.blit(self.score_image,self.score_rect)
		
