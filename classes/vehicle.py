import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100


    def draw(self, screen):
        """draw the vehicle"""
        screen.blit(self.image, self.rect)
        # health bar
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.left, self.rect.top - 10, 100, 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.left, self.rect.top - 10, self.health, 5)) 


    def update(self, position):
        """move the vehicle to follow the mouse"""
        self.rect.center = position

    def takeDamage(self, amount):
        """apply damage to vehicle"""
        self.health -= amount
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        """destroy vehicle"""
        self.kill()