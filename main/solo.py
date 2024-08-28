import pygame
import sys
import random
import main
import button as b

restart = 1

check_errors = pygame.init()
if check_errors[1] > 0:
    print('(Warning!)Found {0} Errors!'.format(check_errors[1]))
    sys.exit(-1)
else:
    print('(+)PyGame successfully initialized!')

# Play Surface

PlaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Snake Game ')

# Display size

width = PlaySurface.get_width()
height = PlaySurface.get_height()
width -= 1
height -= 1

# Colors

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
violet = pygame.Color(143, 0, 255)

# FPS controller

fpsController = pygame.time.Clock()

score = 0
snake_position = [550, 200]
snake_body = [[550, 200], [540, 200], [530, 200]]

direction = 'RIGHT'
change_to = direction

PlaySurface.fill(white)
gameover_sound = pygame.mixer.Sound("../src/sound_effects/gameover.mp3")
swallow_sound = pygame.mixer.Sound("../src/sound_effects/swallo.mp3")
death_sound = pygame.mixer.Sound("../src/sound_effects/lose.wav")


# Game over function
def game_over():

    pygame.mixer.Sound.play(gameover_sound)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        PlaySurface.fill(black)
        g_font = pygame.font.SysFont('Arial Black', 150)
        g_osurf = g_font.render('Game over!', True, red)
        g_orect = g_osurf.get_rect()
        g_orect.midtop = (width / 2, (height / 2) - 300)
        PlaySurface.blit(g_osurf, g_orect)
        show_score(0)

        clicked = b.buttons("Restart", white, (width/2) - 200, (height/2) + 200, 30)
        if clicked:
            start()

        clicked = b.buttons("Back", white, (width/2) + 200, (height/2) + 200, 30)
        if clicked:
            main.home()

        pygame.display.flip()
        pygame.display.update()


def show_score(choice=1):
    s_font = pygame.font.SysFont('monaco', 50)
    sf_font = pygame.font.SysFont('monaco', 80)
    ssurf = s_font.render('Score : {0}'.format(score), True, blue)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (150, 25)
    else:
        ssurf = sf_font.render('Score : {0}'.format(score), True, white)
        srect.midtop = (width / 2 - 50, height / 2)
    PlaySurface.blit(ssurf, srect)


def start():

    global score, snake_position, snake_body, direction, change_to
    score = 0
    snake_position = [550, 200]
    snake_body = [[550, 200], [540, 200], [530, 200]]

    food_position = [int(random.randrange(515, width - 515) / 10) * 10, int(random.randrange(115, height - 115) / 10) * 10]
    food_spawn = True

    life = 3

    direction = 'RIGHT'
    change_to = direction
    life_img = pygame.image.load("../src/icons/life.png").convert()
    death_img = pygame.image.load("../src/icons/death.png").convert()

    PlaySurface.fill(black)
    # Main Logic of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_SPACE:
                    resume()
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Validation of Directions
        if change_to == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if change_to == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        # More on Directions OR Snake Position
        if direction == 'RIGHT':
            snake_position[0] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10

        # Snake Body Mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            pygame.mixer.Sound.play(swallow_sound)
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [int(random.randrange(515, width - 515) / 10) * 10,
                             int(random.randrange(115, height - 115) / 10) * 10]
        food_spawn = True

        # Drawings
        PlaySurface.fill(black)

        rem = 3 - life
        x = 100
        for i in range(life):
            PlaySurface.blit(life_img, (x, 100))
            x += 50
        x = 200
        for i in range(rem):
            PlaySurface.blit(death_img, (x, 100))
            x -= 50

        pygame.draw.line(PlaySurface, red, (500, 100), (width - 500, 100), 5)
        pygame.draw.line(PlaySurface, red, (500, height - 100), (width - 500, height - 100), 5)

        pygame.draw.line(PlaySurface, red, (500, 100), (500, height - 100), 5)
        pygame.draw.line(PlaySurface, red, (width - 500, 100), (width - 500, height - 100), 5)

        for pos in snake_body:
            pygame.draw.rect(PlaySurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(PlaySurface, violet, pygame.Rect(food_position[0], food_position[1], 10, 10))

        if snake_position[0] >= width - 500 or snake_position[0] < 500:
            life -= 1
            reset()
        if snake_position[1] >= height - 100 or snake_position[1] < 100:
            life -= 1
            reset()

        if snake_position[0] >= width or snake_position[0] < 0:
            life -= 1
            reset()
        if snake_position[1] >= height or snake_position[1] < 0:
            life -= 1
            reset()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                life -= 1
                reset()

        if life == 0:
            game_over()

        clicked = b.buttons("Back", white, (width / 2) + 400, (height / 2) + 350, 25)
        if clicked:
            main.home()

        g_font = pygame.font.SysFont('Arial Black', 50)
        g_osurf = g_font.render('Snake Game', True, green)
        g_orect = g_osurf.get_rect()
        g_orect.midtop = (width / 2, 15)
        PlaySurface.blit(g_osurf, g_orect)

        # common stuff
        show_score()
        pygame.display.flip()
        if score >= 20:
            fpsController.tick(30)
        elif score >= 40:
            fpsController.tick(40)
        elif score >= 60:
            fpsController.tick(50)
        elif score >= 80:
            fpsController.tick(60)
        else:
            fpsController.tick(20)


def reset():

    global snake_position, snake_body, score, direction, change_to
    snake_position = [550, 200]
    pygame.mixer.Sound.play(death_sound)
    if score != 0:
        score -= 1
        snake_body.pop()
        x, y = 550, 200
        total = 3 + score
        for i in range(total):
            snake_body[i][0] = x
            snake_body[i][1] = y
            x -= 10
    else:
        snake_body = [[550, 200], [540, 200], [530, 200]]

    direction = 'RIGHT'
    change_to = direction


def resume():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        clicked = b.buttons("Back", white, (width / 2) + 400, (height / 2) + 350, 25)
        if clicked:
            main.home()
