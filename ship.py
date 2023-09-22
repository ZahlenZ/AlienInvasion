import pygame

class Ship():
    def __init__(self, screen, settings):
        """Initialize the ship and set its starting position

        Args:
            screen (screen object): pygame screen object
        """
        self.screen = screen
        self.settings = settings
        
        # Load the ship image and get its rect
        self.image = pygame.image.load("images/space-ship-small.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Update the ships position based no the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
            
        self.rect.centerx = self.center