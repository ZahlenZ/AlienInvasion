import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game, settings, and screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.name)
    # Intialize the clock and running
    clock = pygame.time.Clock()
    # Make a ship
    ship = Ship(screen, ai_settings)
    bullets = Group()
    
    while True:        
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, clock, ship, bullets)

    
run_game()