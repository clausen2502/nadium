import pygame

class AudioManager:
    def __init__(self):
        self.background_music = pygame.mixer.Sound('assets/von_dutch.wav')

    def play_music(self):
        self.background_music.play(loops=-1)
    
    def stop_music(self):
        self.background_music.stop()