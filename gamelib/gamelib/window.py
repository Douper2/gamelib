import pygame
from pygame import clock, screen

def window_res(int):
    pygame.display.set_mode()

def game_fps(int):
    clock.tick()

def fill_screen(str):
    screen.fill()

def init():
    pygame.init()

def close_window():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def quit():
    pygame.quit()

def get_window_size(tuple):
    pygame.get.window_size(tuple)

def set_window_size(tuple):
    pygame.set_window_size(tuple)

def get_window_caption(str):
    pygame.display.get_caption(str)

def set_window_caption(str):
    pygame.display.set_caption(str)

def set_window_fullscreen(bool):
    pygame.display.set_fullscreen(bool)

