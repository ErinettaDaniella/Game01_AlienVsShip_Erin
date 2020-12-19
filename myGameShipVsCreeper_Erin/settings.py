class Settings:

	def __init__(self):
		#Arena Settings
		self.window_width = 800
		self.window_height = 600
		self.bg_color = (5, 40, 120)

		#Ship Settings
		self.ship_speed = 1.0
		self.ship_life = 5


		#Bullets Settings
		self.bullet_speed = 4.0
		self.bullet_width = 50
		self.bullet_height = 15
		self.bullet_color = (255, 242, 178)
		self.bullet_capacity = 9

		#Creeper Settings
		self.creeper_life = 3
		self.creeper_speed = 0.2
		self.creeper_drop_speed = 30
		self.creeper_direction = 1   # 1 to the right, -1 to the left

#color1: 0-255  #brightness
#color2: 0-255  #thickness
#color3: