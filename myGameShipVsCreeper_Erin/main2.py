import pygame
import sys
import random
from time import Sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from creeper import Creeper
from star import Star
from game_stats import GameStats


class AlienWorld:

	def __init__(self):
		pygame.init()
		self.my_settings = Settings()

		self.error = False
		self.screen = pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])
		#self.screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
		self.title = pygame.display.set_caption("Game ALIEN")
		self.bg_color = self.my_settings.bg_color

		self.my_ship = Ship(self)
		self.bullets = pygame.sprite.Group() #container for bullet
		self.creeper_army = pygame.sprite.Group()
		self.my_stars = pygame.sprite.Group()

		self.my_stats = myStats(self)


		self.create_creeper_army()
		self.create_my_stars()


	def run_game(self):
		while not self.error:
			self.check_events() #refactoring
			self.update_ship()
			self.update_bullet()
			self.update_creeper()
			self.remove_bullet()
			self.update_frame() #refactoring

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#sys.exit()
				self.error = True
			elif event.type == pygame.KEYDOWN:
				self.check_keydown_event(event) #refactoring

			elif event.type == pygame.KEYUP:
				self.check_keyup_event(event) #refactoring
				

	def check_keydown_event(self, event):
		if event.key == pygame.K_w: #forward
			self.my_ship.moving_up = True
		elif event.key == pygame.K_s: #backward
			self.my_ship.moving_down = True
		elif event.key == pygame.K_d: #right
			self.my_ship.moving_right = True
		elif event.key == pygame.K_a: #left
			self.my_ship.moving_left = True
		elif event.key == pygame.K_q: #quit
			self.error = True
		elif event.key == pygame.K_SPACE: #fire!
			self.fire_bullet()
		elif event_key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_RCTRL:
			self.screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
		elif event_key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_SHIFT:
			self.screen = pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])



	def check_keyup_event(self, event):
		if event.key == pygame.K_w:
			self.my_ship.moving_up = False
		elif event.key == pygame.K_s:
			self.my_ship.moving_down = False
		elif event.key == pygame.K_d:
			self.my_ship.moving_right = False
		elif event.key == pygame.K_a:
			self.my_ship.moving_left = False

	def fire_bullet(self):
		if len(self.bullets) < self.my_settings.bullet_capacity: 
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def update_ship(self):
		self.my_ship.update() #piloting ship

		if pygame.sprite.spritecollideany(self.my_ship, self.kecoa_army):
		#	print("Kapal menabrak kecoa")
			self.ship_hit()

	def ship_hit(self):
		self.my_stats.ship_life -= 1

		self.creeper_army.empty()
		self.bullets.empty()

		self.create_creeper_army()
		self.my_ship.re_position_ship()

		sleep(0.5)



	def update_bullet(self):  #remove bullet
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		# print(len(self.bullets))
		self.check_bullet_creeper_collision()
		# collisions = pygame.sprite.groupcollide(self.bullets, self.creeper_army, True, True)

	def check_bullet_creeper_collision():
		= pygame.sprite.spritecollideany(self.my_ship, self.kecoa_army)





	def create_creeper(self, col, row):
		creeper = Creeper(self)
		creeper_width, creeper_height = creeper.rect.size
		creeper.x = creeper_width + (2 * creeper_width * col)
		creeper.rect.x = creeper.x
		creeper.rect.y = creeper_height + (2 * creeper_height * row)
		self.creeper_army.add(creeper)

	def create_creeper_army(self):
		creeper = Creeper(self)
		creeper_width, creeper_height = creeper.rect.size
		available_space_for_creeper = self.my_settings.window_height - (2*creeper_width)
		number_of_creeper = available_space_for_creeper // (2*creeper_width)

		creeper_height = creeper.rect.height
		ship_p1_height = self.my_ship.rect.height
		available_space_for_row = self.my_settings.window_height - (2*creeper_height) - ship_p1_height
		number_of_row = available_space_for_row // (2*creeper_height)

		for every_row in range(number_of_row):
			for each_creeper in range(number_of_creeper+1):
				self.create_creeper(each_creeper, every_row)


	def update_creeper(self):
		self.check_creeper_army()
		self.creeper_army.update()

	def check_creeper_army(self):
		for creeper in self.creeper_army.sprites():
			if creeper.check_life():
				self.creeper_army.delete()
			if creeper.check_edges():
				self.change_direction_creeper_army()
				break

	def change_direction_creeper_army(self):
		for creeper in self.creeper_army.sprites():
			creeper.rect.y += self.my_settings.creeper_drop_speed
		self.my_settings.creeper_direction *= -1


	def create_star(self, pos_x, pos_y):
		star = Star(self)
		star.rect.x, star.rect.y = pos_x, pos_y
		self.my_stars.add(star)

	def create_my_stars(self):  #mendapatkan jumlah bintang jika masuk semua
		star = Star(self)
		star_width, star_height = star.rect.size
		number_of_stars = (self.my_settings.window_width * self.my_settings.window_height)//(star_width*star_height)

		for each_star in range(number_of_stars//5):
			pos_x = random.randint(0, self.my_settings.window_width)
			pos_y = random.randint(0, self.my_settings.window_height)
			self.create_star(pos_x, pos_y)


	def update_frame(self):
		self.screen.fill(self.bg_color)
		self.my_stars.draw(self.screen)

		self.my_ship.blit_ship()

		for bullet in self.bullets.sprites():
			bullet.draw()

		self.creeper_army.draw(self.screen)

		pygame.display.flip()


Game_ALIEN = AlienWorld()
Game_ALIEN.run_game()





"""
	def create_creeper(self, number_of_creeper, number_of_row):
		pass



	def create_creeper_army(self):
		creeper = Creeper(self)
		creeper_width = creeper.rect.width
		available_space_for_creeper = self.my_settings.window_width - (2*creeper_width)
		number_of_creeper = available_space_for_creeper // (2*creeper_width)

		creeper_height = creeper.rect.height
		ship_p1_height = self.my_ship.rect.height
		available_space_for_row = self.my_settings.window_height - (2*creeper_height) - ship_p1_height
		number_of_row = available_space_for_row // (2*creeper_height)



		for every_row in range(number_of_row):
			for each_creeper in range(number_of_creeper+1):
				creeper = Creeper(self)
				creeper_width = creeper.rect.width
				creeper_height = creeper.rect.height
				creeper.x = creeper_width + (2 * creeper_width * each_creeper)
				creeper.y = creeper_height + (2 * creeper_height * number_of_row)
				creeper.rect.x = creeper.x
				creeper.rect.y = creeper.y
				self.creeper_army.add(creeper) #keranjang
"""
