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

running = True
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False


    screen.fill((0, 0, 0))

    surf_center =(
        (screen_width - player.surf.get_width())/2,
        (screen_height - player.surf.get_width())/2
    )
    screen.blit(player.surf, player.rect)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    
    pygame.display.update()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0: 
            self.rect.left = 0
        if self.rect.K_RIGHT > screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        if self.rect.top <= 0:
            self.rect.top = 0