import pygame
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

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
    player.update()

pressed_keys = pygame.key.get_pressed()
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

