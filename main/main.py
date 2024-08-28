import pygame
import sys
import button as b
import solo
import duo

check_errors = pygame.init()
if check_errors[1] > 0:
    print('(Warning!)Found {0} Errors!'.format(check_errors[1]))
    sys.exit(-1)
else:
    print('(+)PyGame successfully initialized!')

# screen resolution
PlaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width = PlaySurface.get_width()
height = PlaySurface.get_height()

# caption
pygame.display.set_caption("Home")

clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


def home():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        PlaySurface.fill(black)
        g_font = pygame.font.SysFont('Arial Black', 150)
        g_osurf = g_font.render('Snake Game', True, red)
        g_rect = g_osurf.get_rect()
        g_rect.midtop = (width / 2, (height / 2) - 400)
        PlaySurface.blit(g_osurf, g_rect)

        clicked = b.buttons("SOLO PLAY", white, int(width / 2), (height / 2), 50)
        if clicked:
            solo.start()

        clicked = b.buttons("DUO PLAY", white, int(width / 2), (height / 2) + 100, 50)
        if clicked:
            duo.menu()

        # Exit Button
        x, y, f = 1400, 700, 70
        clicked = b.buttons("Exit", white, x, y, f)

        if clicked:
            sys.exit()

        g_font = pygame.font.SysFont('Arial Black', 20)
        g_osurf = g_font.render('Press [SPACE] to pause/resume the game', True, green)
        g_rect = g_osurf.get_rect()
        g_rect.midtop = (width / 2, (height / 2) + 300)
        PlaySurface.blit(g_osurf, g_rect)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    home()
