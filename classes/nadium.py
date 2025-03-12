import pygame

class Nadium(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.pos_y = float(self.rect.y)

    def draw(self, screen):
        """draw Nadium"""
        screen.blit(self.image, self.rect)