import pygame

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flying Enemy Territory')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

player = Player()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and (
                event.type == pygame.K_ESCAPE or pygame.K_q
            )):
            pygame.quit()
            quit()

while True:
    screen.fill((0, 0, 0))

    surf_center =(
        (screen_width - player.surf.get_width())/2,
        (screen_height - player.surf.get_width())/2
    )
    screen.blit(player.surf, player.rect)

    event_handler()
    pygame.display.update()