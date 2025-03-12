import pygame
from classes.button import Button
from gameLogic import GameLogic
from data import Data
from classes.vehicle import Vehicle

class Menu():
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.FPS = 1000
        self.running = True

        # screen settings
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("NADIUM")

        # load background photo
        self.backgroundPhoto = pygame.image.load("assets/temp_background.png")
        self.backgroundPhoto = pygame.transform.scale(self.backgroundPhoto, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background_height = self.backgroundPhoto.get_height()
        
        # set a data instance
        self.data = Data()

        # set a vehicle instance
        self.vehicle = Vehicle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, "assets/bumblebee.png")

    
    def main_menu(self):
        """main loop for menu"""
        while self.running:
            self.SCREEN.blit(self.backgroundPhoto, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # draw vehicle
            self.vehicle.show_vehicle(self.SCREEN)

            # title and buttons
            NADIUM_TEXT = self.get_font(100).render("NADIUM", True, "#b68f40")
            MENU_RECT = NADIUM_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/play_rect.png"), pos=(640, 250), 
                                 text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/quit_rect.png"), pos=(640, 550), 
                                 text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            
            self.SCREEN.blit(NADIUM_TEXT, MENU_RECT)

            # show highscore
            highscore = str(self.data.getHighscore()) 
            HIGHSCORE_TEXT = self.get_font(30).render(f"HIGHSCORE: {highscore}", True, "#00FFFF")
            HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(640, 650))
            self.SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.running = False

            pygame.display.update()
            self.clock.tick(self.FPS)

    def play(self):
        game_logic = GameLogic(self.SCREEN, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        game_logic.play()

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)