class Settings:
	""" A class to store all the settings of Allien Invesion."""
	def __init__(self):
		"""Initializing settings values."""
		#Screen settings
		self.screen_width = 1150
		self.screen_height = 650
		self.bg_color = (230,230,230)
		self.ship_speed = 1.5
		
		#Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
		
		#ship settings 
		self.alien_speed = 0.2
		self.fleet_drop_speed = 60
		self.ship_limit = 3
		
		#fleet direction 1 represents right and -1 represents left
		self.fleet_direction = 1
		
		
		
