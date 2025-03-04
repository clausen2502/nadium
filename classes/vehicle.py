import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        self.rect = self.image.get_rect(center=(x, y))


    def draw(self, screen):
        """draw the vehicle"""
        screen.blit(self.image, self.rect)

    def update(self, position):
        """move the vehicle to follow the mouse"""
        self.rect.center = position

    def takeDamage(self):
        pass