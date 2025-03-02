import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("NADIUM")

nadium_photo = pygame.image.load("nadium.png")

def main_menu():
    while True:
        SCREEN.blit(nadium_photo, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()