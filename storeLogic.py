import pygame

class StoreLogic:
    def __init__(self, data_manager):
        self.data = data_manager
        self.vehicles = self.data.getAllVehicles()
        self.vehicle_images = self._preload_images()
        self.owned_vehicle = self.data.getAllOwnedVehicles()

    def _preload_images(self):
        images = {}
        for vehicle in self.vehicles:
            img = pygame.image.load(vehicle.image)
            img = pygame.transform.scale(img, (100, 50))
            images[vehicle.name] = img
        return images

    def get_vehicles(self):
        return self.vehicles

    def get_vehicle_image(self, name):
        return self.vehicle_images.get(name)
    
    def is_owned(self, name: str) -> bool:
        for vehicle in self.owned_vehicle:
            if vehicle.name == name:
                return True
        return False
    
    def buy_vehicle(self, vehicle):
        """Adds the vehicle to the player's owned vehicles list"""
        if self.is_owned(vehicle.name):
            print(f"{vehicle.name} is already owned.")
            return
        # Add the vehicle to JSON
        self.data.buyVehicle(vehicle.name, vehicle.image)

        # Update in-memory state
        self.owned_vehicle.append(vehicle)
