import pygame
from data import Data

class StoreUI():
    def __init__(self, screen, screen_width, screen_height):
        pygame.init()
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

        # set a vehicle item instance

    def showStore(self):
        """Show the store background and main loop functions"""
        while self.viewingStore:
            self.screen.blit(self.storeBackground, (0, 0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # title and buttons

            # main loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.viewingStore = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.viewingStore = False
            pygame.display.update()
            self.clock.tick(self.FPS)


    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)