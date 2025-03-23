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

        # scroll settings
        self.scroll_offset = 0
        self.scroll_speed = 500

        # load arrow photos
        self.left_arrow = pygame.image.load("assets/left_arrow.png")
        self.right_arrow = pygame.image.load("assets/right_arrow.png")

        self.left_arrow = pygame.transform.scale(self.left_arrow, (50, 50))
        self.right_arrow = pygame.transform.scale(self.right_arrow, (50, 50))

        # Position arrows centered under vehicle selection
        arrow_y = 400
        arrow_spacing = 100
        self.left_arrow_rect = self.left_arrow.get_rect(center=(self.screen_width // 2 - arrow_spacing, arrow_y))
        self.right_arrow_rect = self.right_arrow.get_rect(center=(self.screen_width // 2 + arrow_spacing, arrow_y))

    def showInventory(self):
        """Show the inventory layout and main loop functions"""
        while self.viewingInventory:
            self.screen.blit(self.inventoryBackground, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            x_pos = 250
            y_pos = 250
            owned_vehicles = self.inventory.get_vehicles()
            for vehicle in self.inventory.get_vehicles():
                # skip drawing image if it's way off screen for optimization
                draw_x = x_pos - self.scroll_offset
                if draw_x < -300 or draw_x > self.screen_width + 300:
                    x_pos += self.scroll_speed
                    continue
                
                # vehicle image
                vehicle_image = self.inventory.get_vehicle_image(vehicle.name)
                vehicle_image_rect = vehicle_image.get_rect(center=(draw_x, y_pos - 50))
                self.screen.blit(vehicle_image, vehicle_image_rect)


                vehicle_text = self.get_font(30).render(vehicle.name, True, "#b68f40")
                vehicle_text_rect = vehicle_text.get_rect(center=(draw_x, y_pos + 20))
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
                    pos=(draw_x, y_pos + 80),
                    text_input=button_text,
                    font=self.get_font(25),
                    base_color=button_color,
                    hovering_color="white")

                if button.checkForInput(MENU_MOUSE_POS) and pygame.mouse.get_pressed()[0]:
                    self.inventory.select_vehicle(vehicle.name)

                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

                x_pos += 400

            # blit arrows
            self.screen.blit(self.left_arrow, self.left_arrow_rect)
            self.screen.blit(self.right_arrow, self.right_arrow_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.viewingInventory = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.viewingInventory = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        MENU_MOUSE_POS = pygame.mouse.get_pos()
                        if self.left_arrow_rect.collidepoint(MENU_MOUSE_POS):
                            self.scroll_offset = max(0, self.scroll_offset - self.scroll_speed)
                        elif self.right_arrow_rect.collidepoint(MENU_MOUSE_POS):
                            max_scroll = max(0, (len(owned_vehicles) * 300) - self.screen_width + 250)
                            self.scroll_offset = min(max_scroll, self.scroll_offset + self.scroll_speed)


            
            pygame.display.update()
            self.clock.tick(self.FPS)

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)