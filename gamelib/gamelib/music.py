import pygame

def music(filename, music_file):
    pygame.mixer.init()

def play(filename, music_file):
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()