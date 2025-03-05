import pygame
import time

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100
        self.last_damage_time = 0
        self.invincibility_duration = 1
        self.flicker_interval = 0.3
        self.invincible = False

    def draw(self, screen):
        """draw the vehicle"""
        screen.blit(self.image, self.rect)
        # health bar
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.left, self.rect.bottom + 5, 100, 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.left, self.rect.bottom + 5, self.health, 5)) 

    def update(self, position):
        """move the vehicle to follow the mouse"""
        self.rect.center = position

    def take_damage(self, amount):
        """apply damage to vehicle"""
        current_time = time.time()
        if self.invincible == False:
            self.last_damage_time = current_time
            self.health -= amount
            self.invincible = True
            print(f"Took damage, new vehicle health: {self.health}")
            if self.health <= 0:
                self.destroy()
            else:
                print("Invincible, no damage taken")
                self.update_invincibility()

    def destroy(self):
        """destroy vehicle"""
        self.kill()

    def update_invincibility(self):
        """make the vehicle invincible for a few seconds after colliding with obstacle"""
        if self.invincible == True:
            current_time = time.time()
        
            if int(current_time * 10) % 2 == 0:
                grayscale_image = pygame.transform.grayscale(self.original_image)
                self.image = pygame.transform.scale(grayscale_image, (self.rect.size))
            else:
                self.image = pygame.transform.scale(self.original_image, (self.rect.size))
        
            if current_time - self.last_damage_time >= self.invincibility_duration:
                self.invincible = False
                print("Invincibility ended")
                