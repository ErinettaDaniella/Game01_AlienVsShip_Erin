import pygame
from pygame.sprite import Sprite

class Creeper(Sprite):

	def __init__(self, AlienWorld):
		super().__init__()
		self.life = 2
		self.screen = AlienWorld.screen
		self.settings = AlienWorld.my_settings

		self.image = pygame.image.load('img/creeper.png')
		self.rect = self.image.get_rect()

		#posisi sementara
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#variable untuk simpan x sebagai data float
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		self.x += (self.settings.creeper_speed * self.settings.creeper_direction)
		self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def check_life(self):
		if self.settings.creeper_life == 0:
			return True