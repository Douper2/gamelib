import pygame

def play_music(filename, music_file):
    pygame.mixer.load()
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()
