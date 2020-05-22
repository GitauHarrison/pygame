import pygame

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flying Enemy Territory')

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and (
                event.type == pygame.K_ESCAPE or pygame.K_q
            )):
            pygame.quit()
            quit()

while True:
    screen.fill((255, 255, 255))
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    
    surf_center =(
        (screen_width - surf.get_width())/2,
        (screen_height - surf.get_width())/2
    )
    screen.blit(surf, surf_center)

    event_handler()
    pygame.display.update()