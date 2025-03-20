import pygame
from data import Data
from classes.button import Button

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
        # create a "select" and "currently selected" button, which can be clicked to switch vehicles.
        # make a button that changes color on hover
        CURRENTLY_SELECTED_BUTTON = Button(image=pygame.image.load("assets/play_rect.png"), pos=(x_pos, y_pos), 
                            text_input="SELECT", font=self.get_font(75), base_color="#32CD32", hovering_color="White")
        SELECT_BUTTON = Button(image=pygame.image.load("assets/quit_rect.png"), pos=(x_pos, y_pos - 50), 
                            text_input="QUIT", font=self.get_font(75), base_color="#FFD700", hovering_color="White")
       
        while self.viewingInventory:
            self.screen.blit(self.inventoryBackground, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # iterate over all vehicles owned in data, show them in order, be able to 
            # select from different ones that are owned. Can't select one that is not owned.
            owned_vehicles = self.data.getAllOwnedVehicles()
            x_pos = 250
            y_pos = 250
            # find all names in vehicles owned
            for vehicle in owned_vehicles:
                # load name from vehicle data and show it
                vehicle_text = self.get_font(30).render(vehicle.name, True, "#b68f40")
                vehicle_rect = vehicle_text.get_rect(center=(x_pos, y_pos))
                
                # load image from vehicle data and show it
                vehicle_image = pygame.image.load(vehicle.image)
                vehicle_image = pygame.transform.scale(vehicle_image, (100, 50))
                vehicle_image_rect = vehicle_image.get_rect(center=(x_pos, y_pos - 50))

                self.screen.blit(vehicle_text, vehicle_rect)
                self.screen.blit(vehicle_image, vehicle_image_rect)
                

            # main loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.viewingInventory = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.viewingInventory = False
            pygame.display.update()
            self.clock.tick(self.FPS)

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)