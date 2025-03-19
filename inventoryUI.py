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

        # title and buttons

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