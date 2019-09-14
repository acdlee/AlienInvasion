import pygame	#used for actually making the game

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	#Initialize game and create a screen object
	pygame.init()	#initializes background settings for pygame to work
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height) )
	pygame.display.set_caption("Alien Invasion")

	#Make a ship, group of bullets, and a group of aliens
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	#Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, aliens)

	#Start the main loop of the game
	while True:

		#watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		#Update screen
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()