import pygame
import math
from classes.button import Button
from classes.vehicle import Vehicle
from gameLogic import GameLogic
from data import Data
from audioManager import AudioManager


class Menu():
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.FPS = 300
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

        # set a vehicle instance
        self.vehicle = Vehicle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, "assets/bumblebee.png")

        # add the vehicle to a sprite group
        self.vehicle_group = pygame.sprite.GroupSingle(self.vehicle)

        # set a data instance
        self.data = Data()

        # set the audio manager
        self.audio = AudioManager()
    
    def render(self):
        """draw the menu background and scroll"""
        for i in range(self.tiles):
            self.SCREEN.blit(self.backgroundPhoto, (0, (i - 1) * self.SCREEN_HEIGHT + self.scroll))
        
        # scroll background
        self.scroll += 1

        # reset scroll
        if abs(self.scroll) > self.background_height:
            self.scroll = 0
    
    def main_menu(self):
        """main loop for menu"""
        while self.running:
            self.SCREEN.blit(self.backgroundPhoto, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # PLAY and QUIT buttons
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

            # show current vehicle
            self.vehicle.show_vehicle(self.SCREEN)

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
        """Play the game loop"""
        game_logic = GameLogic(self.vehicle, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        playing = True
        while playing:
            self.SCREEN.fill((0, 0, 0))
            self.render()
            
            # play the music
            self.audio.play_music()

            # update vehicle position
            MOUSE_POS = pygame.mouse.get_pos()
            self.vehicle.update(MOUSE_POS)

            # update game logic (obstacles and collisions)
            game_logic.update()

            # draw vehicle and obstacles
            self.vehicle.draw(self.SCREEN)
            game_logic.draw(self.SCREEN)

             # show distance travelled
            DISTANCE_TRAVELLED_TEXT = self.get_font(15).render("DISTANCE TRAVELLED:", True, "#d7fcd4")
            DISTANCE_RECT = DISTANCE_TRAVELLED_TEXT.get_rect(center=(640, 20))
            self.SCREEN.blit(DISTANCE_TRAVELLED_TEXT, DISTANCE_RECT)
            total_distance = str(game_logic.calculate_distance_travelled()) + "M"
            TOTAL_DISTANCE_TEXT = self.get_font(15).render(total_distance, True, "#d7fcd4")
            TOTAL_DISTANCE_RECT = TOTAL_DISTANCE_TEXT.get_rect(center=(640, 40))
            self.SCREEN.blit(TOTAL_DISTANCE_TEXT, TOTAL_DISTANCE_RECT)

            # check for new highscore
            self.data.updateHighscore(total_distance)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        playing = False
                        self.vehicle.reset(MENU_MOUSE_POS)
                        self.audio.stop_music()
            if self.vehicle.health == 0:
                playing = False
                self.vehicle.reset(MENU_MOUSE_POS)
                self.audio.stop_music()
            pygame.display.flip()
            self.clock.tick(self.FPS)


    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)