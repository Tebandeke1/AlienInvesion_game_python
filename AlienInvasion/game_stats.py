class GameStats:
	"""Track the statistics for alien invasion """
	
	def __init__(self,ai_game):
		"""Initialize statistics"""
		self.sett = ai_game.settings
		self.reset_stats()
		
		#Start an alien version in an active state
		
		"""Start game in an inactive state"""
		self.game_active = False
		
		"""High score should never be reset"""
		self.high_score = 0
		
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game"""
		self.ship_left = self.sett.ship_limit
		self.score = 0
		self.level = 1
