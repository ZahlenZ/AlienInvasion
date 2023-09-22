import sys

import pygame

from bullet import Bullet

def check_events(ship, settings, screen, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
            
def check_keydown_events(event, ship, settings, screen, bullets):
    """Respond to Key Presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        shoot_bullets(bullets, settings, screen, ship)
    # if event.key == pygame.K_SPACE and len(bullets) < settings.bullets_allowed:
    #     new_bullet = Bullet(screen, settings, ship)
    #     bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    """Repons to Key Release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
            
            
def update_screen(settings, screen, clock, ship, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
    clock.tick(60)
    

def shoot_bullets(bullets, settings, screen, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(screen, settings, ship)
        bullets.add(new_bullet)
    
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)