import pygame
from data import Data
from classes.button import Button
from inventoryLogic import InventoryLogic


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

        # set a inventory logic instance
        self.inventory = InventoryLogic(self.data)

    def showInventory(self):
        """Show the inventory layout and main loop functions"""
        while self.viewingInventory:
            self.screen.blit(self.inventoryBackground, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            x_pos = 250
            y_pos = 250
            for vehicle in self.inventory.get_vehicles():
                vehicle_image = self.inventory.get_vehicle_image(vehicle.name)
                vehicle_image_rect = vehicle_image.get_rect(center=(x_pos, y_pos - 50))
                self.screen.blit(vehicle_image, vehicle_image_rect)

                vehicle_text = self.get_font(30).render(vehicle.name, True, "#b68f40")
                vehicle_text_rect = vehicle_text.get_rect(center=(x_pos, y_pos + 20))
                self.screen.blit(vehicle_text, vehicle_text_rect)

                
                is_selected = self.inventory.is_selected(vehicle.name)
                button_rect = pygame.image.load("assets/play_rect.png")
                if is_selected:
                    button_rect = pygame.transform.scale(button_rect, (220, 40))
                else:
                    button_rect = pygame.transform.scale(button_rect, (200, 40))

                button_text = "SELECTED" if is_selected else "SELECT"
                button_color = "#32CD32" if is_selected else "#FFD700"

                button = Button(
                    image=button_rect,
                    pos=(x_pos, y_pos + 80),
                    text_input=button_text,
                    font=self.get_font(25),
                    base_color=button_color,
                    hovering_color="white")

                if button.checkForInput(MENU_MOUSE_POS) and pygame.mouse.get_pressed()[0]:
                    self.inventory.select_vehicle(vehicle.name)

                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

                x_pos += 400

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