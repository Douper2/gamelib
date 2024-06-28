import pygame
from pygame import clock, screen

def window_res(int):
    pygame.display.set_mode(int)

def game_fps(int):
    clock.tick(int)

def fill_screen(str):
    screen.fill(str)

def init():
    pygame.init()

def close_window():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def quit():
    pygame.quit()

def get_window_size(str):
    pygame.get.window_size(str)

def set_window_size(str):
    pygame.set_window_size(str)

def get_window_caption(str):
    pygame.display.get_caption(str)

def set_window_caption(str):
    pygame.display.set_caption(str)

def set_window_fullscreen(bool):
    pygame.display.set_fullscreen(bool)
