class GameStats:
	"""Track the statistics for alien invasion """
	
	def __init__(self,ai_game):
		"""Initialize statistics"""
		self.sett = ai_game.settings
		self.reset_stats()
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game"""
		self.ship_left = self.sett.ship_limit
