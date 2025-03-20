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
        self.invincibility_duration = 2.4
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
        position = self.limit_vehicle(position)
        self.rect.center = position
        

    def take_damage(self, amount):
        """apply damage to vehicle"""
        current_time = time.time()
        if self.invincible == False:
            self.last_damage_time = current_time
            self.health -= amount
            self.invincible = True
            self.tinted_image = self.tint_image(self.original_image, (255, 0, 0, 100)) # set the tinted image
            print(f"Took damage, new vehicle health: {self.health}")
            if self.health <= 0:
                self.destroy()

    def destroy(self):
        """destroy vehicle"""
        self.kill()

    def update_invincibility(self):
        """make the vehicle invincible for a few seconds after colliding with obstacle"""
        if self.invincible == True:
            current_time = time.time()
            if int((current_time - self.last_damage_time) / self.flicker_interval) % 2 == 0:
                self.image = pygame.transform.scale(self.tinted_image, (self.rect.size))
            else:
                self.image = pygame.transform.scale(self.original_image, (self.rect.size))

            if current_time - self.last_damage_time >= self.invincibility_duration:
                self.invincible = False
                self.image = pygame.transform.scale(self.original_image, self.rect.size)
                print("Invincibility ended")

    def tint_image(self, image, tint_color):
        """applies tint to the vehicle with a specific color"""
        tinted_image = image.copy()  
        tint_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(tint_color)
        tinted_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted_image

    def reset(self, mouse_position):
        """resets the vehicle to its original state when restarting game"""
        self.health = 100
        self.invincible = False
        self.image = pygame.transform.scale(self.original_image, self.rect.size)
        self.last_damage_time = 0
        self.rect.center = mouse_position

    def limit_vehicle(self, position):
        """sets a x limit that the vehicle cant reach"""
        min_x = 250
        max_x = 1030
        x, y = position
        if x <= min_x:
            x = min_x
        if x >= max_x:
            x = max_x
        return (x, y)

    def show_vehicle(self, screen):
        """show the current selected vehicle"""
        VEHICLE_RECT = (585, 375)
        screen.blit(self.image, VEHICLE_RECT)
    
    def __repr__(self):
        return f"Vehicle(name='{self.name}', image='{self.image}'"