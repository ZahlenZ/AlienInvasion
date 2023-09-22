import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired from a ship"""
    def __init__(self, screen, settings, ship):
        """Createa a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0,0) and then set corect position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store bullets position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)