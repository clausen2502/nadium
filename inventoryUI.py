import pygame
from data import Data

class InventoryUI():
    def __init__(self, screen, screen_width, screen_height):
        pygame.init
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.font = pygame.font.Font("assets/font.ttf", 30)
        self.title_pos = (self.screen_width // 2, 100)

        self.clock = pygame.time.Clock()
        self.FPS = 1000
        self.viewingInventory = True

        # load background photo
        self.inventoryBackground = pygame.image.load("assets/inventory.png")
        self.inventoryBackground = pygame.transform.scale(self.inventoryBackground, (self.screen_width, self.screen_height))

        # set a data instance
        self.data = Data()

    def showInventory(self):
        """Show the inventory layout and main loop functions"""
        while self.viewingInventory:
            self.screen.blit(self.inventoryBackground, (0, 0))
            pygame.display.update()
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # iterate over all vehicles owned in data, show them in order, be able to 
            # select from different ones that are owned. Can't select one that is not owned.
            vehicle_data = self.data.getAllVehicles()
        
            # find all names in vehicles owned
            vehicles = []
            for vehicle in vehicle_data:
                vehicles.append(vehicle["name"])
            
            for vehicle in vehicles:
                    vehicle_text = self.get_font(50).render(vehicle["name"])


            # title and buttons
            NADIUM_TEXT = self.get_font(100).render("NADIUM", True, "#b68f40")
            MENU_RECT = NADIUM_TEXT.get_rect(center=(640, 100))
            store_rect = pygame.image.load("assets/play_rect.png")
            store_rect = pygame.transform.scale(store_rect, (180, 60))
            inventory_rect = pygame.image.load("assets/inventory_rect.png")
            inventory_rect = pygame.transform.scale(inventory_rect, (180, 60))

            # main loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.viewingInventory = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.viewingInventory = False
                pygame.display.update()
                self.clock.tick(self.FPS)

    def increment_rect(self):
        pass

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)