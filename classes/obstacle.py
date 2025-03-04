import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        x = random.randint(0, self.SCREEN_WIDTH)
        y = random.randint(0, self.SCREEN_HEIGHT)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        """draw the vehicle"""
        screen.blit(self.image, self.rect)