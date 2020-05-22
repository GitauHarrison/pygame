import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
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
    event_handler()
    pygame.display.update()