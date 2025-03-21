import pygame


class InventoryLogic:
    def __init__(self, data_manager):
        self.data = data_manager
        self.vehicles = self.data.getAllOwnedVehicles()
        self.selected_vehicle = self.data.getSelectedVehicleName()
        self.vehicle_images = self._preload_images()

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

    def is_selected(self, name):
        return self.selected_vehicle == name

    def select_vehicle(self, name):
        self.selected_vehicle = name
        self.data.setSelectedVehicleName(name)