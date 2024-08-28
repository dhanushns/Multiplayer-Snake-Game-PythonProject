import pygame

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(WARNING) Found {0} Errors!".format(check_errors))
else:
    print("(+)Pygame Successfully initialized")

PlaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

button_sound = pygame.mixer.Sound("../src/sound_effects/button.mp3")

clock = pygame.time.Clock()

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
Dark_Orange = (255, 140, 0)
light_green = (0, 128, 0)


def buttons(name, color, x, y, f):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x - f <= mouse_pos[0] <= x + f and y <= mouse_pos[1] <= y + f:

        sfont = pygame.font.SysFont("arial", f)
        srender = sfont.render(name, True, orange)
        srect = srender.get_rect()
        srect.midtop = (x, y)
        PlaySurface.blit(srender, srect)

        if mouse_click[0]:
            pygame.mixer.Sound.play(button_sound)
            return True

    else:

        sfont = pygame.font.SysFont("arial", f)
        srender = sfont.render(name, True, color)
        srect = srender.get_rect()
        srect.midtop = (x, y)
        PlaySurface.blit(srender, srect)


def select_buttons(x, y, width, height):

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, width, height),2)

        if mouse_click[0]:
            return True
