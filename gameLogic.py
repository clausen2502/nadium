import random
import pygame
from classes.obstacle import Obstacle
from classes.nadium import Nadium
from data import Data
import time
import math


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

        # screen settings
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("NADIUM")

        # load background photo
        self.backgroundPhoto = pygame.image.load("assets/temp_background.png")
        self.backgroundPhoto = pygame.transform.scale(self.backgroundPhoto, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background_height = self.backgroundPhoto.get_height()

        # define game variables
        self.scroll = 0.0
        self.tiles = math.ceil(self.SCREEN_WIDTH / self.background_height) + 1

    def spawn_obstacles(self, num):
        """creates an obstacle at a random x-position"""
        for i in range(num):
            x = random.randint(250, self.screen_width - 250)
            y = -50
            obstacle = Obstacle("assets/asteroid1.png", x, y)
            obstacle.pos_y = float(obstacle.rect.y)
            self.obstacles.add(obstacle)

    def spawn_nadium(self, num):
        """creates nadium at a random x-position"""
        for i in range(num):
            x = random.randint(250, self.screen_width - 250)
            y = -50
            nadium = Nadium("assets/nadium.png", x, y)
            nadium.pos_y = float(nadium.rect.y)
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
            self.data.addNadiumToBalance(1)
            self.nadium.remove(collided_nadium)

    def update(self):
        """update obstacles based on scroll speed"""
        elapsed_time = int(time.time() - self.game_start_time)
        # max speed reaches after 3 min 33 seconds
        self.scroll_speed = min(4.0, 1 + (elapsed_time // 10) * 0.15) # gradually increase every 10 seconds 
        previous_speed = round(self.scroll_speed)  # store the current speed

        # calculate new speed
        self.scroll_speed = min(10, 1 + (elapsed_time // 5) * 0.2)

        # only print if it actually changed
        if round(self.scroll_speed) != previous_speed:
            print(f"Scroll speed increased to: {self.scroll_speed}")

        self.obstacle_spawn_timer() # run the obstacle spawn timer
        for obstacle in self.obstacles:
            obstacle.pos_y += self.scroll_speed
            obstacle.rect.y = int(obstacle.pos_y)  

            # remove off screen obstacles
            if obstacle.rect.top > self.screen_height:
                self.obstacles.remove(obstacle)

        self.nadium_spawn_timer() # run the nadium spawn timer
        for nadium in self.nadium:
            nadium.pos_y += self.scroll_speed
            nadium.rect.y = int(nadium.pos_y)

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

    def render(self):
        """draw the menu background and scroll"""
        for i in range(self.tiles):
            self.SCREEN.blit(self.backgroundPhoto, (0, (i - 1) * self.SCREEN_HEIGHT + int(self.scroll)))
        
        # scroll background
        self.scroll += self.scroll_speed

        # reset scroll
        if abs(self.scroll) > self.background_height:
            self.scroll = 0

    def calculate_distance_travelled(self):
        """calculate the distance travelled"""
        elapsed_time = int((time.time() - self.game_start_time) * 100)
        return elapsed_time

    def obstacle_spawn_timer(self):
        """obstacle spawn timer logic"""
        base_delay = 60
        speed_factor = self.scroll_speed
        spawn_delay = max(10, int(base_delay - (speed_factor - 1) * 14))
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