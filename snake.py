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
snek_speed = 12
font_style = pygame.font.SysFont(None,50)

#drawSanke
def draw_snek(snek_block, snek_list):
    for x in snek_list:
        pygame.draw.rect(screen,GREEN, [x[0], x[1], snek_block, snek_block])
#mssg
def message(msg, color):
    messg = font_style.render(msg, True, color)
    screen.blit(messg, [screen_w/6, screen_h / 3])
#game func
    
def game():
    game_over = False
    game_close = False

    x1 = screen_w/2
    y1 = screen_h/2

    x1_change = 0
    y1_change = 0

    snek_list = []
    snek_length = 1

    #foodposition
    foodx = round(random.randrange(0, screen_w - snek_block)/20.0) * 20.0
    foody = round(random.randrange(0, screen_h - snek_block)/20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message("LOSER! C to restart and Q to quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snek_block
                    y1_change = 0
                elif  event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snek_block
                    y1_change = 0
                elif  event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snek_block
                    x1_change = 0
                elif  event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snek_block
                    x1_change = 0 

        if x1 >= screen_w or x1< 0 or y1 >= screen_h or y1 < 0:
            game_close = True
        x1 += x1_change 
        y1 += y1_change 

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [foodx, foody, snek_block, snek_block])
        snek_head = []
        snek_head.append(x1)
        snek_head.append(y1)
        snek_list.append(snek_head)
        
        if len(snek_list) > snek_length:
            del snek_list[0]

        for x in snek_list[:-1]:
            if x == snek_head:
                game_close = True

        draw_snek(snek_block, snek_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_w - snek_block)/20.0) * 20.0
            foody = round(random.randrange(0, screen_h - snek_block)/20.0) * 20.0
            snek_length += 1

        pygame.display.update()

        pygame.time.Clock().tick(snek_speed)
    
    pygame.quit()
    quit()  

game()




