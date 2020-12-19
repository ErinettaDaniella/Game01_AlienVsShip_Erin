class GameStats:

	def __init__(self, AlienWorld):
		self.setting = ALienWorld.my_settings
		self.reset_stats()

	def reset_stats(self):
		self.ship_life = self.my_settings.ship_life