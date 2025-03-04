import pygame

class Vehicle():
    def __init__(self, x, y, image_path):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        """draw the vehicle"""
        screen.blit(self.image, self.rect)

    def moveVehicle(self, position):
        """move the vehicle to follow the mouse"""
        self.rect.center = position

    def takeDamage(self):
        pass