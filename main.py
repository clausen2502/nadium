from UI import Menu
from gameLogic import GameLogic
import pygame

def main():
    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("NADIUM")

    # Create game logic first (this gives us access to the selected vehicle)
    game = GameLogic(screen, screen_width, screen_height)

    # Pass the selected vehicle to the menu
    ui = Menu(screen, screen_width, screen_height, game.vehicle)

    ui.main_menu()

if __name__ == "__main__":
    main()
