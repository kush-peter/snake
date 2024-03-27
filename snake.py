import pygame 
import random

pygame.init()
#screen banai idhar
screen_w = 800
screen_h = 600
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Rio ka Snek game")
#color consts
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#mySnake
snek_block = 20
snek_speed = 15
font_style = pygame.font.SysFont(None,50)

#drawSanke
def draw_snek(snek_block, snek_list):
    for i in snek_list:
        pygame.draw.rect(screen,GREEN, [x[0], x[1]], snek_block, snek_block)
#mssg
def message(msg, color):
    messg = font_style.render(msg, True, color)
    screen.blit(messg, [screen_w/ 6, screen_h / 3])
#game func
    
def game():
    game_over = False
    game_close = False

    x1 = screen_w/2
    y1 = screen_h/2

    x1.change = 0
    y1.change = 0

    snek_list = []
    snek_length = 1

    #foodposition
    foodx = round(random.randrange(0, screen_w - snek_block)/20.0) * 20.0
    foody = round(random.randrange(0, screen_h - snek_block)/20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message("LOSER! Dum daba ke bhaagne ke liye Q dabaye, Firse khelne ke liye C", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame

