import random
import pygame
from classes.obstacle import Obstacle
from classes.nadium import Nadium
from data import Data
import time



class GameLogic:
    def __init__(self, vehicle, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.vehicle = vehicle
        self.obstacles = pygame.sprite.Group()
        self.nadium = pygame.sprite.Group()
        self.vehicle_group = pygame.sprite.GroupSingle(self.vehicle)
        self.game_start_time = time.time()
        self.obstacle_spawn_timer_count = 0
        self.nadium_spawn_timer_count = 0
        self.scroll_speed = 1
        self.data = Data()
        

    def spawn_obstacles(self, num):
        """creates an obstacle at a random x-position"""
        for i in range(num):
            x = random.randint(250, self.screen_width - 250)
            y = -50
            obstacle = Obstacle("assets/asteroid1.png", x, y)
            self.obstacles.add(obstacle)

    def spawn_nadium(self, num):
        """creates nadium at a random x-position"""
        for i in range(num):
            x = random.randint(250, self.screen_width - 250)
            y = -50
            nadium = Nadium("assets/nadium.png", x, y)
            self.nadium.add(nadium)


    def check_obstacle_collisions(self):
        """check if any obstacle hits the vehicle"""
        collided_obstacle = pygame.sprite.spritecollideany(self.vehicle, self.obstacles, pygame.sprite.collide_mask)
        if collided_obstacle and not self.vehicle.invincible:
                print("Collision detected!")
                self.vehicle.take_damage(25)
                self.obstacles.remove(collided_obstacle)
    
    def check_nadium_collisions(self):
        """check if nadium hits the vehicle"""
        collided_nadium = pygame.sprite.spritecollideany(self.vehicle, self.nadium, pygame.sprite.collide_mask)
        if collided_nadium and not self.vehicle.invincible:
            print("Nadium collected")
            self.data.addNadiumToBalance(1)
            self.nadium.remove(collided_nadium)

    def update(self):
        """update obstacles based on scroll speed"""
        elapsed_time = int(time.time() - self.game_start_time)
        self.obstacle_spawn_timer() # run the obstacle spawn timer
        for obstacle in self.obstacles:
            obstacle.rect.y += self.scroll_speed

            # remove off screen obstacles
            if obstacle.rect.top > self.screen_height:
                self.obstacles.remove(obstacle)

        self.nadium_spawn_timer() # run the nadium spawn timer
        for nadium in self.nadium:
            nadium.rect.y += self.scroll_speed

            # remove off screen nadium
            if nadium.rect.top > self.screen_height:
                self.nadium.remove(nadium)
        self.check_obstacle_collisions()
        self.check_nadium_collisions()
        self.vehicle.update_invincibility()

    def draw(self, screen):
        """draw obstacles"""
        self.obstacles.draw(screen)
        self.nadium.draw(screen)

    def calculate_distance_travelled(self):
        """calculate the distance travelled"""
        elapsed_time = int((time.time() - self.game_start_time) * 100)
        return elapsed_time

    def obstacle_spawn_timer(self):
        """obstacle spawn timer logic"""
        spawn_delay = 60
        if self.obstacle_spawn_timer_count >= spawn_delay:
            self.spawn_obstacles(1)
            self.obstacle_spawn_timer_count = 0
        self.obstacle_spawn_timer_count += 1 
    
    def nadium_spawn_timer(self):
        """nadium spawn timer logic"""
        spawn_delay = 500
        if self.nadium_spawn_timer_count >= spawn_delay:
            self.spawn_nadium(1)
            self.nadium_spawn_timer_count = 0
        self.nadium_spawn_timer_count += 1
    
    def validate_spawn(self, nadium_x, obstacle_x):
        """validate spawn between Nadium and Obstacle"""
        pass