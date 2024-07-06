import pygame

def draw_rectangle(surface, color, rect):
    pygame.draw.rect(surface, color, rect)

def draw_polygon(surface, color, points):
    pygame.draw.polygon(surface, color, points)

def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

def draw_sline(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos)

