import pygame
from data import Data
from storeLogic import StoreLogic
from classes.button import Button

class StoreUI():
    def __init__(self, screen, screen_width, screen_height):
        pygame.init
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.font = pygame.font.Font("assets/font.ttf", 30)
        self.title_pos = (self.screen_width // 2, 100)

        self.clock = pygame.time.Clock()
        self.FPS = 1000
        self.viewingStore = True
        
        # load background photo
        self.storeBackground = pygame.image.load("assets/STORE.png")
        self.storeBackground = pygame.transform.scale(self.storeBackground, (self.screen_width, self.screen_height))

        # set a data instance
        self.data = Data()

        # set a store logic instance
        self.store = StoreLogic(self.data)

        # scroll settings
        self.scroll_offset = 0
        self.vehicle_spacing = 400
        self.scroll_speed = self.vehicle_spacing
        self.vehicle_start_x = 250

        
        # arrow settings
        arrow_y = 680
        arrow_spacing = 100

        # load and scale base arrow images
        self.left_arrow = pygame.image.load("assets/left_arrow.png")
        self.left_arrow = pygame.transform.scale(self.left_arrow, (50, 50))
        self.right_arrow = pygame.image.load("assets/right_arrow.png")
        self.right_arrow = pygame.transform.scale(self.right_arrow, (50, 50))

        self.left_arrow_btn = Button(
            image=self.left_arrow,
            pos=(self.screen_width // 2 - arrow_spacing, arrow_y),
            text_input="",
            font=self.get_font(10),
            base_color=(255, 255, 255),  # ignored 
            hovering_color=(255, 255, 255))  # ignored 

        self.right_arrow_btn = Button(
            image=self.right_arrow,
            pos=(self.screen_width // 2 + arrow_spacing, arrow_y),
            text_input="",
            font=self.get_font(10),
            base_color=(255, 255, 255), # ignored 
            hovering_color=(255, 255, 255)) # ignored 

        # Load hover images
        self.left_arrow_hover = pygame.image.load("assets/left_arrow_hover.png")
        self.left_arrow_hover = pygame.transform.scale(self.left_arrow_hover, (50, 50))

        self.right_arrow_hover = pygame.image.load("assets/right_arrow_hover.png")
        self.right_arrow_hover = pygame.transform.scale(self.right_arrow_hover, (50, 50))

    def showStore(self):
        """Show the store layout and main loop functions"""
        while self.viewingStore:
            self.screen.blit(self.storeBackground, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            x_pos = self.vehicle_start_x
            y_pos = 250
            store_vehicles = self.store.get_vehicles()
            for vehicle in store_vehicles:
                # skip drawing image if it's way off screen for optimization
                draw_x = x_pos - self.scroll_offset
                if draw_x < -300 or draw_x > self.screen_width + 300:
                    x_pos += self.scroll_speed
                    continue
                
                # vehicle image
                vehicle_image = self.store.get_vehicle_image(vehicle.name)
                vehicle_image_rect = vehicle_image.get_rect(center=(draw_x, y_pos - 50))
                self.screen.blit(vehicle_image, vehicle_image_rect)

                vehicle_text = self.get_font(30).render(vehicle.name, True, "#b68f40")
                vehicle_text_rect = vehicle_text.get_rect(center=(draw_x, y_pos + 20))
                self.screen.blit(vehicle_text, vehicle_text_rect)

                is_owned = self.store.is_owned(vehicle.name)
                button_rect = pygame.image.load("assets/play_rect.png")
                if is_owned:
                    button_rect = pygame.transform.scale(button_rect, (220, 40))
                else:
                    button_rect = pygame.transform.scale(button_rect, (200, 40))

                button_text = "OWNED" if is_owned else "BUY"
                button_color = "#FFD700" if is_owned else "#00C851"

                button = Button(
                    image=button_rect,
                    pos=(draw_x, y_pos + 80),
                    text_input=button_text,
                    font=self.get_font(25),
                    base_color=button_color,
                    hovering_color=button_color if is_owned else "white")

                if button.checkForInput(MENU_MOUSE_POS) and pygame.mouse.get_pressed()[0]:
                    self.store.buy_vehicle(vehicle)

                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

                x_pos += self.vehicle_spacing

            # blit arrows
            # Hover effect for arrows
            if self.left_arrow_btn.checkForInput(MENU_MOUSE_POS):
                self.left_arrow_btn.image = self.left_arrow_hover
            else:
                self.left_arrow_btn.image = self.left_arrow

            if self.right_arrow_btn.checkForInput(MENU_MOUSE_POS):
                self.right_arrow_btn.image = self.right_arrow_hover
            else:
                self.right_arrow_btn.image = self.right_arrow

            # draw buttons
            self.left_arrow_btn.update(self.screen)
            self.right_arrow_btn.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.viewingStore = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.viewingStore = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.left_arrow_btn.checkForInput(MENU_MOUSE_POS):
                            self.scroll_offset = max(0, self.scroll_offset - self.scroll_speed)
                        elif self.right_arrow_btn.checkForInput(MENU_MOUSE_POS):
                            vehicles_visible = self.screen_width // self.vehicle_spacing
                            max_scroll = max(0, (len(store_vehicles) - vehicles_visible) * self.vehicle_spacing)
                            self.scroll_offset = min(max_scroll, self.scroll_offset + self.scroll_speed)

            pygame.display.update()
            self.clock.tick(self.FPS)

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)