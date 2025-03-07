import random
import pygame
from classes.obstacle import Obstacle


class GameLogic:
    def __init__(self, vehicle, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.vehicle = vehicle
        self.obstacles = pygame.sprite.Group()
        self.vehicle_group = pygame.sprite.GroupSingle(self.vehicle)
        print(f"GameLogic received vehicle ID: {id(self.vehicle)}")
        print(f"GameLogic vehicle from group ID: {id(self.vehicle_group.sprite)}")
    
    def spawn_obstacles(self, num):
        """creates an obstacle at a random x-position"""
        for i in range(num):
            x = random.randint(250, self.screen_width - 250)
            y = -50  # start off-screen
            obstacle = Obstacle("assets/asteroid1.png", x, y)
            self.obstacles.add(obstacle)


    def check_collisions(self):
        """check if any obstacle hits the vehicle"""
        collided_obstacle = pygame.sprite.spritecollideany(self.vehicle, self.obstacles, pygame.sprite.collide_mask)
        if collided_obstacle and not self.vehicle.invincible:
                print("Collision detected!")
                self.vehicle.take_damage(25)
                self.obstacles.remove(collided_obstacle)

    def update(self, scroll_speed):
        """update obstacles based on scroll speed"""
        for obstacle in self.obstacles:
            obstacle.rect.y += scroll_speed

            # remove off screen obstacles
            if obstacle.rect.top > self.screen_height:
                self.obstacles.remove(obstacle)
        self.check_collisions()
        self.vehicle.update_invincibility()

    def draw(self, screen):
        """draw obstacles and vehicle"""
        self.obstacles.draw(screen)

    def 