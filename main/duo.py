import pygame
import sys
import random
import button as b
import main

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
orange = pygame.Color(255, 165, 0)
violet = pygame.Color(143, 0, 255)

# FPS controller
fpsController = pygame.time.Clock()

PlaySurface.fill(white)

player_1_score = 0
player_2_score = 0

color1 = white
color2 = white

swallow_sound = pygame.mixer.Sound("../src/sound_effects/swallo.mp3")
victory_sound = pygame.mixer.Sound("../src/sound_effects/victory.wav")
death_sound = pygame.mixer.Sound("../src/sound_effects/lose.wav")
draw_sound = pygame.mixer.Sound("../src/sound_effects/draw.mp3")
health_sound = pygame.mixer.Sound("../src/sound_effects/health.wav")

life_img = pygame.image.load("../src/icons/life.png")
death_img = pygame.image.load("../src/icons/death.png")

player_1_snake_pos = [350, 700]
player_1_snake_body = [[350, 700], [340, 700], [330, 700]]

player_2_snake_pos = [350, 200]
player_2_snake_body = [[350, 200], [340, 200], [330, 200]]

direction_1 = 'RIGHT'
change_to_1 = direction_1

direction_2 = 'RIGHT'
change_to_2 = direction_1

player_1_life = 3
player_2_life = 3


def menu():
    PlaySurface.fill(black)
    global color1, color2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if color1 != white and color2 != white:
                    if event.key == pygame.K_RETURN:
                        start(color1, color2)
        g_font = pygame.font.SysFont('Arial Black', 150)
        g_osurf = g_font.render('Snake Game', True, red)
        g_rect = g_osurf.get_rect()
        g_rect.midtop = (width / 2, (height / 2) - 400)
        PlaySurface.blit(g_osurf, g_rect)

        g_font = pygame.font.SysFont('Arial Black', 50)
        g_osurf = g_font.render('Choose your snake color', True, white)
        g_rect = g_osurf.get_rect()
        g_rect.midtop = (width / 2, (height / 2) - 100)
        PlaySurface.blit(g_osurf, g_rect)

        g_font = pygame.font.SysFont('Arial Black', 35)
        g_osurf = g_font.render('Player 1 : ', True, color1)
        g_rect = g_osurf.get_rect()
        g_rect.midtop = ((width / 2) - 100, (height / 2) + 100)
        PlaySurface.blit(g_osurf, g_rect)

        x, y, w, h = (width / 2) + 20, (height / 2) + 115, 30, 30
        pygame.draw.rect(PlaySurface, red, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color2 != red:
                color1 = red
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        x, y, w, h = (width / 2) + 80, (height / 2) + 115, 30, 30
        pygame.draw.rect(PlaySurface, blue, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color2 != blue:
                color1 = blue
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        x, y, w, h = (width / 2) + 140, (height / 2) + 115, 30, 30
        pygame.draw.rect(PlaySurface, green, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color2 != green:
                color1 = green
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        x, y, w, h = (width / 2) + 200, (height / 2) + 115, 30, 30
        pygame.draw.rect(PlaySurface, orange, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color2 != orange:
                color1 = orange
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        g_font = pygame.font.SysFont('Arial Black', 35)
        g_osurf = g_font.render('Player 2 : ', True, color2)
        g_rect = g_osurf.get_rect()
        g_rect.midtop = ((width / 2) - 100, (height / 2) + 170)
        PlaySurface.blit(g_osurf, g_rect)

        x, y, w, h = (width / 2) + 20, (height / 2) + 185, 30, 30
        pygame.draw.rect(PlaySurface, red, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color1 != red:
                color2 = red
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        x, y, w, h = (width / 2) + 80, (height / 2) + 185, 30, 30
        pygame.draw.rect(PlaySurface, blue, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color1 != blue:
                color2 = blue
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        x, y, w, h = (width / 2) + 140, (height / 2) + 185, 30, 30
        pygame.draw.rect(PlaySurface, green, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color1 != green:
                color2 = green
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        x, y, w, h = (width / 2) + 200, (height / 2) + 185, 30, 30
        pygame.draw.rect(PlaySurface, orange, pygame.Rect(x, y, w, h))
        clicked = b.select_buttons(x, y, w, h)
        if clicked:
            if color1 != orange:
                color2 = orange
            pygame.draw.rect(PlaySurface, white, pygame.Rect(x, y, w, h), 5)

        if color1 != white and color2 != white:
            clicked = b.buttons("START", white, (width / 2), (height / 2) + 300, 50)
            if clicked:
                start(color1, color2)

        clicked = b.buttons("Back", white, (width / 2) + 400, (height / 2) + 350, 25)
        if clicked:
            main.home()

        pygame.display.flip()
        pygame.display.update()
        fpsController.tick(60)


# Game over function
def gameover(victory_player, match, color):

    if match == 1:
        pygame.mixer.Sound.play(victory_sound)

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
        g_font = pygame.font.SysFont('Arial Black', 120)
        g_osurf = g_font.render('Game over!', True, red)
        g_orect = g_osurf.get_rect()
        g_orect.midtop = (width / 2, 50)
        PlaySurface.blit(g_osurf, g_orect)
        show_score(0)
        pygame.mixer.Sound.stop(death_sound)
        g_font = pygame.font.SysFont('Arial Black', 80)
        if match == 1:
            g_osurf = g_font.render("{0} WON THE MATCH".format(victory_player), True, color)
        else:
            g_osurf = g_font.render("DRAW MATCH", True, white)
            pygame.mixer.Sound.play(draw_sound)
        g_orect = g_osurf.get_rect()
        g_orect.midtop = (width / 2, height / 2 + 50)
        PlaySurface.blit(g_osurf, g_orect)

        clicked = b.buttons("Restart", white, (width / 2) - 300, (height / 2) + 250, 30)
        if clicked:
            start(player1_color=color1, player2_color=color2)

        clicked = b.buttons("Back", white, (width / 2) + 300, (height / 2) + 250, 30)
        if clicked:
            main.home()

        pygame.display.flip()
        pygame.display.update()


def show_score(choice=1):
    global color1, color2
    s_font = pygame.font.SysFont('monaco', 50)
    sf_font = pygame.font.SysFont('monaco', 60)
    ssurf = s_font.render('Player_1 Score  {0}'.format(player_1_score), True, color1)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (150, 20)
    else:
        ssurf = sf_font.render('Player_1 Score : {0}'.format(player_1_score), True, color1)
        srect.midtop = (width / 2 - 50, 300)
    PlaySurface.blit(ssurf, srect)

    s_font = pygame.font.SysFont('monaco', 50)
    sf_font = pygame.font.SysFont('monaco', 60)
    ssurf = s_font.render('{0}  Player_2 Score'.format(player_2_score), True, color2)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (1450, 20)
    else:
        ssurf = sf_font.render('Player_2 Score : {0}'.format(player_2_score), True, color2)
        srect.midtop = (width / 2 - 50, 400)
    PlaySurface.blit(ssurf, srect)


def start(player1_color, player2_color):

    global player_1_score, player_2_score, player_1_snake_body, player_2_snake_body, player_1_snake_pos, player_2_snake_pos
    global change_to_1, change_to_2, direction_1, direction_2, player_1_life, player_2_life
    player_1_score = 0
    player_2_score = 0

    player_1_life = 3
    player_2_life = 3

    player_1_total_life = 3
    player_2_total_life = 3

    # Important variables
    player_1_snake_pos = [350, 700]
    player_1_snake_body = [[350, 700], [340, 700], [330, 700]]

    player_2_snake_pos = [350, 200]
    player_2_snake_body = [[350, 200], [340, 200], [330, 200]]

    food_position = [int(random.randrange(315, width - 315) / 10) * 10,
                     int(random.randrange(115, height - 115) / 10) * 10]
    food_spawn = True

    life_position = [int(random.randrange(315, width - 315) / 10) * 10,
                     int(random.randrange(115, height - 115) / 10) * 10]
    life_spawn = True

    random_time = int(random.randrange(5, 15))
    spawn_time = 5
    m_sec = 0
    sec = 0
    flag = False

    direction_1 = 'RIGHT'
    change_to_1 = direction_1

    direction_2 = 'RIGHT'
    change_to_2 = direction_1

    PlaySurface.fill(black)

    # Main Logic of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to_1 = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    change_to_1 = 'LEFT'
                if event.key == pygame.K_UP:
                    change_to_1 = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to_1 = 'DOWN'
                if event.key == pygame.K_d:
                    change_to_2 = 'RIGHT'
                if event.key == pygame.K_a:
                    change_to_2 = 'LEFT'
                if event.key == pygame.K_w:
                    change_to_2 = 'UP'
                if event.key == pygame.K_s:
                    change_to_2 = 'DOWN'
                if event.key == pygame.K_SPACE:
                    resume()
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Validation of Directions
        if change_to_1 == 'RIGHT' and not direction_1 == 'LEFT':
            direction_1 = 'RIGHT'
        if change_to_1 == 'LEFT' and not direction_1 == 'RIGHT':
            direction_1 = 'LEFT'
        if change_to_1 == 'UP' and not direction_1 == 'DOWN':
            direction_1 = 'UP'
        if change_to_1 == 'DOWN' and not direction_1 == 'UP':
            direction_1 = 'DOWN'

        if change_to_2 == 'RIGHT' and not direction_2 == 'LEFT':
            direction_2 = 'RIGHT'
        if change_to_2 == 'LEFT' and not direction_2 == 'RIGHT':
            direction_2 = 'LEFT'
        if change_to_2 == 'UP' and not direction_2 == 'DOWN':
            direction_2 = 'UP'
        if change_to_2 == 'DOWN' and not direction_2 == 'UP':
            direction_2 = 'DOWN'

        # More on Directions OR Snake Position
        if direction_1 == 'RIGHT':
            player_1_snake_pos[0] += 10
        if direction_1 == 'LEFT':
            player_1_snake_pos[0] -= 10
        if direction_1 == 'UP':
            player_1_snake_pos[1] -= 10
        if direction_1 == 'DOWN':
            player_1_snake_pos[1] += 10

        if direction_2 == 'RIGHT':
            player_2_snake_pos[0] += 10
        if direction_2 == 'LEFT':
            player_2_snake_pos[0] -= 10
        if direction_2 == 'UP':
            player_2_snake_pos[1] -= 10
        if direction_2 == 'DOWN':
            player_2_snake_pos[1] += 10

        # Snake Body Mechanism
        player_1_snake_body.insert(0, list(player_1_snake_pos))
        if player_1_snake_pos[0] == food_position[0] and player_1_snake_pos[1] == food_position[1]:
            pygame.mixer.Sound.play(swallow_sound)
            player_1_score += 1
            food_spawn = False
        else:
            player_1_snake_body.pop()

        player_2_snake_body.insert(0, list(player_2_snake_pos))
        if player_2_snake_pos[0] == food_position[0] and player_2_snake_pos[1] == food_position[1]:
            pygame.mixer.Sound.play(swallow_sound)
            player_2_score += 1
            food_spawn = False
        else:
            player_2_snake_body.pop()

        if not food_spawn:
            food_position = [int(random.randrange(315, width - 315) / 10) * 10,
                             int(random.randrange(115, height - 115) / 10) * 10]
        food_spawn = True

        if player_1_snake_pos[0] == life_position[0] and player_1_snake_pos[1] == life_position[1]:
            pygame.mixer.Sound.play(swallow_sound)
            if player_1_life < 3:
                player_1_life += 1
                pygame.mixer.Sound.play(health_sound)
                x = 100
                for i in range(player_1_life):
                    pygame.draw.rect(PlaySurface, green, pygame.Rect(x, 100, 10, 10))
                    x += 20
                    player_1_total_life += 1
            life_spawn = False

        if player_2_snake_pos[0] == life_position[0] and player_2_snake_pos[1] == life_position[1]:
            pygame.mixer.Sound.play(swallow_sound)
            if player_2_life < 3:
                player_2_life += 1
                pygame.mixer.Sound.play(health_sound)
                x = 1400
                for i in range(player_2_life):
                    pygame.draw.rect(PlaySurface, green, pygame.Rect(x, 100, 10, 10))
                    x += 20
                    player_2_total_life += 1
            life_spawn = False

        if not life_spawn:
            random_time = int(random.randrange(5, 15))
            life_position = [int(random.randrange(315, width - 315) / 10) * 10,
                             int(random.randrange(115, height - 115) / 10) * 10]
        life_spawn = True

        # Drawings
        PlaySurface.fill(black)

        if sec == random_time:
            flag = True
            sec = 0
        m_sec += 1
        if m_sec == 20:
            sec += 1
            m_sec = 0

        if flag:
            if spawn_time <= 100:
                pygame.draw.rect(PlaySurface, green, pygame.Rect(life_position[0], life_position[1], 10, 10))
                spawn_time += 1
            else:
                spawn_time = 0
                flag = False

        player_1_remaining_life = 3 - player_1_life
        player_1_life_axis = 100
        for i in range(player_1_life):
            PlaySurface.blit(life_img, (player_1_life_axis, 100))
            player_1_life_axis += 50
        player_1_life_axis = 200
        for i in range(player_1_remaining_life):
            PlaySurface.blit(death_img, (player_1_life_axis, 100))
            player_1_life_axis -= 50

        player_2_remaining_life = 3 - player_2_life
        player_2_life_axis = 1400
        for i in range(player_2_life):
            PlaySurface.blit(life_img, (player_2_life_axis, 100))
            player_2_life_axis += 50
        player_2_life_axis = 1500
        for i in range(player_2_remaining_life):
            PlaySurface.blit(death_img, (player_2_life_axis, 100))
            player_2_life_axis -= 50

        pygame.draw.line(PlaySurface, red, (300, 100), (width - 300, 100), 5)
        pygame.draw.line(PlaySurface, red, (300, height - 100), (width - 300, height - 100), 5)

        pygame.draw.line(PlaySurface, red, (300, 100), (300, height - 100), 5)
        pygame.draw.line(PlaySurface, red, (width - 300, 100), (width - 300, height - 100), 5)

        for pos in player_1_snake_body:
            pygame.draw.rect(PlaySurface, player1_color, pygame.Rect(pos[0], pos[1], 10, 10))

        for pos in player_2_snake_body:
            pygame.draw.rect(PlaySurface, player2_color, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(PlaySurface, violet, pygame.Rect(food_position[0], food_position[1], 10, 10))

        if player_1_snake_pos[0] >= width - 300 or player_1_snake_pos[0] < 300:
            snakes_life(1, "self")

        if player_1_snake_pos[1] >= height - 100 or player_1_snake_pos[1] < 100:
            snakes_life(1, "self")

        if player_2_snake_pos[0] >= width - 300 or player_2_snake_pos[0] < 300:
            snakes_life(2, "self")

        if player_2_snake_pos[1] >= height - 100 or player_2_snake_pos[1] < 100:
            snakes_life(2, "self")

        for block in player_1_snake_body[1:]:
            if player_1_snake_pos[0] == block[0] and player_1_snake_pos[1] == block[1]:
                snakes_life(1, "self")

        for block in player_2_snake_body[1:]:
            if player_2_snake_pos[0] == block[0] and player_2_snake_pos[1] == block[1]:
                snakes_life(2, "self")

        for block in player_1_snake_body:
            if player_2_snake_body[0] == block:
                snakes_life(2, "kill")

        for block in player_2_snake_body:
            if player_1_snake_body[0] == block:
                snakes_life(1, "kill")

        if player_1_life == 0 or player_2_life == 0:
            if player_1_score > player_2_score:
                gameover("PLAYER 1", 1, color1)
            elif player_2_score > player_1_score:
                gameover("PLAYER 2", 1, color2)
            else:
                gameover("DRAW", 0, white)

        clicked = b.buttons("Back", white, (width / 2) + 600, (height / 2) + 350, 25)
        if clicked:
            menu()

        g_font = pygame.font.SysFont('Arial Black', 50)
        g_osurf = g_font.render('Snake Game', True, green)
        g_orect = g_osurf.get_rect()
        g_orect.midtop = (width / 2, 15)
        PlaySurface.blit(g_osurf, g_orect)

        # common stuff
        show_score()
        pygame.display.flip()
        pygame.display.update()
        fpsController.tick(15)


def snakes_life(player, death):

    global player_1_score, player_2_score, player_1_snake_body, player_2_snake_body, player_1_snake_pos, player_2_snake_pos
    global change_to_1, change_to_2, direction_1, direction_2, player_1_life, player_2_life
    pygame.mixer.Sound.play(death_sound)
    if player == 1:
        direction_1 = 'RIGHT'
        change_to_1 = direction_1
        if death == "self":
            player_1_life -= 1
            if player_1_score != 0:
                player_1_score -= 1
                player_1_snake_body.pop()
        elif death == "kill":
            if player_1_life == 1:
                player_1_life = 0
            else:
                player_1_life -= 2
            player_2_life -= 1
            if player_1_score != 0:
                player_1_snake_body.pop()
                player_1_score -= 1
        player_1_snake_pos = [350, 700]

        if player_1_score == 0:
            player_1_snake_body = [[350, 700], [340, 700], [330, 700]]
        else:
            x, y = 350, 700
            total = 3 + player_1_score
            for i in range(total):
                player_1_snake_body[i][0] = x
                player_1_snake_body[i][1] = y
                x -= 10

    elif player == 2:
        direction_2 = 'RIGHT'
        change_to_2 = direction_2
        if death == "self":
            player_2_life -= 1
            player_2_snake_body.pop()
            if player_2_score != 0:
                player_2_score -= 1
        elif death == "kill":
            if player_2_life == 1:
                player_2_life = 0
            else:
                player_2_life -= 2
            player_1_life -= 1
            if player_2_score != 0:
                player_2_snake_body.pop()
                player_2_score -= 1
        player_2_snake_pos = [350, 200]

        if player_2_score == 0:
            player_2_snake_body = [[350, 200], [340, 200], [330, 200]]
        else:
            x, y = 350, 200
            total = 3 + player_2_score
            for i in range(total):
                player_2_snake_body[i][0] = x
                player_2_snake_body[i][1] = y
                x -= 10


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
