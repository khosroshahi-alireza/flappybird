import pygame
import sys

pygame.init()

#All variable
screen_x = 576
screen_y = 1024  
floor_X = 0
background_image = pygame.image.load("assets/img/bg2.png")
background_image = pygame.transform.scale2x(background_image)
floor_image = pygame.image.load('assets/img/floor.png')
floor_image = pygame.transform.scale2x(floor_image)

main_screen = pygame.display.set_mode((screen_x,screen_y))

clock = pygame.time.Clock()

#Game Body
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    floor_X -=1
    main_screen.blit(background_image,(0,0))
    main_screen.blit(floor_image,(floor_X,900))
    main_screen.blit(floor_image,(floor_X + 576,900))
    if floor_X <= -576:
         floor_X = 0 

    pygame.display.update()
    clock.tick(90)
