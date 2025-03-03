import pygame
class Menu():
    def __init__(self):
        pygame.init()

        # screen settings
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("NADIUM")

        # load background photo
        self.menuPhoto = pygame.image.load("assets/menu.png")
        self.menuPhoto = pygame.transform.scale(self.menuPhoto, (1280, 720))
        
        self.running = True

    def start_game(self):
        """handles all pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def render(self):
        """draw the menu background"""
        self.SCREEN.blit(self.menuPhoto, (0, 0))
        pygame.display.update()
    
    def run(self):
        """main loop"""
        while self.running:
            self.start_game()
            self.render()
        pygame.quit()