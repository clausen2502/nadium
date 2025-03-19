import pygame

class VehicleItem:
    def __init__(self, name, image_path, price):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(image_path), (120, 60))  # vehicle size in store 
        self.price = price
        self.image_path = image_path  # image for the vehicle
