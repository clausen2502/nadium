import pygame
import math
from classes.button import Button

clock = pygame.time.Clock()
FPS = 60

class Menu():
    def __init__(self):
        pygame.init()
        
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

        # define game variables
        self.scroll = 0
        self.tiles = math.ceil(self.SCREEN_WIDTH / self.background_height) + 1

    def render(self):
        """draw the menu background and scroll"""
        for i in range(self.tiles):
            self.SCREEN.blit(self.backgroundPhoto, (0, (i - 1) * self.SCREEN_HEIGHT + self.scroll))
        pygame.display.update()
        
        # scroll background
        self.scroll += 0.5

        # reset scroll
        if abs(self.scroll) > self.background_height:
            self.scroll = 0
    
    def main_menu(self):
        """main loop for menu"""
        while self.running:
            self.SCREEN.blit(self.backgroundPhoto, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            NADIUM_TEXT = self.get_font(100).render("NADIUM", True, "#b68f40")
            MENU_RECT = NADIUM_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/play_rect.png"), pos=(640, 250), 
                    text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/quit_rect.png"), pos=(640, 550), 
                    text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            
            self.SCREEN.blit(NADIUM_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
            pygame.display.update()
            clock.tick(FPS)
        
    def play(self):
        """play the game loop"""
        playing = True
        while playing:
            self.render()

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)