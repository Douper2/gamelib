import pygame

def time_wait(int):
    pygame.time.wait(int)

def delay_game(int):
    pygame.time.delay(int)

if isinstance(time_wait(), str):
    print("You put a string instead of an integer in the time_wait() function")

if isinstance(delay_game(), str):
    print("You put a string instead of an integer in the delay_game() function")