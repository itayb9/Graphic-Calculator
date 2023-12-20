import pygame
import math

pygame.init()
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1024

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
center_x = (WINDOW_WIDTH // 2) - 35
center_y = WINDOW_HEIGHT // 2
scale = 7
step = 20
bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
bg.fill(pygame.Color("#ffffff"))


# Drawing the xy plane
def draw_xy_plane():
    pygame.draw.line(current_bg, pygame.Color("#000000"), (center_x, 0), (center_x, WINDOW_WIDTH),
                     2)
    pygame.draw.line(current_bg, pygame.Color("#000000"), (0, center_y), (WINDOW_WIDTH, center_y), 2)


# Reading the functions from the functions.txt file
def read_functions():
    functions = []
    with open('functions.txt', 'r') as file:
        for line in file:
            color_code, function = line.strip().split(';')
            functions.append((color_code, function))
    return functions


# Drawing the functions on the screen
def draw_functions(functions, current_bg):
    for color_code, function in functions:
        color = pygame.Color(color_code)
        point_list = []
        for x in range(WINDOW_WIDTH):
            y = eval(function, {"x": (x - center_x) / scale})
            y = center_y - int(y * scale)
            point_list.append((x, y))
        pygame.draw.lines(current_bg, color, False, point_list, 2)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # For moving in the screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                center_x -= 20 * scale
            if event.key == pygame.K_RIGHT:
                center_x += 20 * scale
            if event.key == pygame.K_UP:
                center_y += 20 * scale
            if event.key == pygame.K_DOWN:
                center_y -= 20 * scale
            if event.key == pygame.K_i:
                scale *= 1.2
            if event.key == pygame.K_o:
                scale /= 1.2

    current_bg = bg.copy()
    draw_xy_plane()
    functions = read_functions()
    draw_functions(functions, current_bg)
    window.blit(current_bg, (0, 0))
    pygame.display.flip()

pygame.quit()