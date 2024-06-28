import pygame

def get_sg_ev():
    pygame.event.poll()

def ev_wait(float):
    pygame.event.wait(float)

def rev_evts():
    pygame.event.clear()

def new_ev(bool):
    pygame.event.post(bool)