import random
import pygame
from classes.obstacle import Obstacle
import time


class GameLogic:
    def __init__(self, vehicle, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.vehicle = vehicle
        self.obstacles = pygame.sprite.Group()
        self.vehicle_group = pygame.sprite.GroupSingle(self.vehicle)
        self.game_start_time = time.time()
        self.spawn_timer_count = 0
        self.scroll_speed = 1

    def spawn_obstacles(self, num):
        """creates an obstacle at a random x-position"""
        for i in range(num):
            x = random.randint(250, self.screen_width - 250)
            y = -50
            obstacle = Obstacle("assets/asteroid1.png", x, y)
            self.obstacles.add(obstacle)


    def check_collisions(self):
        """check if any obstacle hits the vehicle"""
        collided_obstacle = pygame.sprite.spritecollideany(self.vehicle, self.obstacles, pygame.sprite.collide_mask)
        if collided_obstacle and not self.vehicle.invincible:
                print("Collision detected!")
                self.vehicle.take_damage(25)
                self.obstacles.remove(collided_obstacle)

    def update(self):
        """update obstacles based on scroll speed"""
        elapsed_time = int(time.time() - self.game_start_time)
        self.spawn_timer() # run the spawn timer
        for obstacle in self.obstacles:
            obstacle.rect.y += self.scroll_speed

            # remove off screen obstacles
            if obstacle.rect.top > self.screen_height:
                self.obstacles.remove(obstacle)
        self.check_collisions()
        self.vehicle.update_invincibility()


    def draw(self, screen):
        """draw obstacles"""
        self.obstacles.draw(screen)

    def calculate_distance_travelled(self):
        """Calculate the distance travelled"""
        elapsed_time = int((time.time() - self.game_start_time) * 100)
        return elapsed_time

    def spawn_timer(self):
        """Spawn timer logic"""
        spawn_delay = 60
        if self.spawn_timer_count >= spawn_delay:
            self.spawn_obstacles(1)
            self.spawn_timer_count = 0
        self.spawn_timer_count += 1 