import pygame  # importing the pygame library
import random
import config
from config import Players  # importing Players class
from config import Obstacles  # importing Obstacles class
pygame.init()  # initializing pygame
pygame.font.init()
size = (700, 500)  # setting screen size
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# all values are initialized to default values in order to begin a fresh game
tc1 = 0
tc2 = 0
carry = True
level = 1
score1 = 0
score2 = 0
cp = 1
x1 = 0
x2 = 0
x3 = 0
x4 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
speed11 = 1
speed12 = 3
speed21 = 1
speed22 = 3
rnd = 0
time1 = 0
time2 = 0
wp = 0
death1 = 0
death2 = 0

# function to display a message on the screen while suspending other activities
def draw_text(surf, text, size, x, y):
    # font imported from config file
    font = pygame.font.Font(config.font_name, size)
    text_surface = font.render(text, True, config.black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# a few groups are created to classify the sprites into players and obstacles
all_sprites_list = pygame.sprite.Group()
fixobs_list = pygame.sprite.Group()
movobs_list = pygame.sprite.Group()
obs_list = pygame.sprite.Group()

# instances of Players are created with certain images
Player1 = Players("pirate1.png")
Player2 = Players("pirate2.png")
Treasure = Players("chest.png")

# instances of Obstacles are created with certain images
Obstacle1 = Obstacles("bomb.png")
Obstacle2 = Obstacles("dead.png")
Obstacle3 = Obstacles("ship.png")
Obstacle4 = Obstacles("ship.png")
Obstacle0 = Obstacles("dead.png")
Obstacle00 = Obstacles("bomb.png")

# treasure is positioned
Treasure.rect.x = 340
Treasure.rect.y = 184

# players are positioned
Player1.rect.x = 340
Player1.rect.y = 469

Player2.rect.x = 340
Player2.rect.y = 8

# obstacles are positioned
Obstacle00.rect.x = 550
Obstacle00.rect.y = 368
Obstacle0.rect.x = 100
Obstacle0.rect.y = 276
Obstacle1.rect.x = 340
Obstacle1.rect.y = 368
Obstacle2.rect.x = 340
Obstacle2.rect.y = 276
Obstacle3.rect.x = 0
Obstacle3.rect.y = 138
Obstacle4.rect.x = 0
Obstacle4.rect.y = 46

# all sprites are added to respective group
all_sprites_list.add(Treasure)
all_sprites_list.add(Player1)
all_sprites_list.add(Player2)
all_sprites_list.add(Obstacle1)
all_sprites_list.add(Obstacle2)
all_sprites_list.add(Obstacle3)
all_sprites_list.add(Obstacle4)
all_sprites_list.add(Obstacle0)
all_sprites_list.add(Obstacle00)

fixobs_list.add(Obstacle1)
fixobs_list.add(Obstacle2)
fixobs_list.add(Obstacle0)
fixobs_list.add(Obstacle00)

movobs_list.add(Obstacle3)
movobs_list.add(Obstacle4)

obs_list.add(Obstacle1)
obs_list.add(Obstacle2)
obs_list.add(Obstacle3)
obs_list.add(Obstacle4)
obs_list.add(Obstacle0)
obs_list.add(Obstacle00)
# main loop starts
while carry:
    # check if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry = False
    keys = pygame.key.get_pressed()
    # below, the controls for player 1 are defined
    if cp == 1:
        if keys[pygame.K_LEFT]:
            Player1.moveleft(1)
        if keys[pygame.K_RIGHT]:
            Player1.moveright(1)
        if keys[pygame.K_UP]:
            Player1.moveup(1)
        if keys[pygame.K_DOWN]:
            Player1.movedown(1)
    # below, the controls for player 2 are defined
    if cp == 2:
        if keys[ord('a')]:
            Player2.moveleft(1)
        if keys[ord('d')]:
            Player2.moveright(1)
        if keys[ord('w')]:
            Player2.moveup(1)
        if keys[ord('s')]:
            Player2.movedown(1)
    # starts with game logic here
    # first, the ocean and and shores are drawn
    screen.fill(config.blue)
    pygame.draw.rect(screen, config.green, (0, 0, 700, 40), 0)
    pygame.draw.rect(screen, config.green, (0, 460, 700, 40), 0)
    pygame.draw.rect(screen, config.green, (0, 92, 700, 40), 0)
    pygame.draw.rect(screen, config.green, (0, 184, 700, 40), 0)
    pygame.draw.rect(screen, config.green, (0, 276, 700, 40), 0)
    pygame.draw.rect(screen, config.green, (0, 368, 700, 40), 0)
    # if player 1 wins, increase speed for player 1
    # if player 2 wins, increase speed for player 2
    if cp == 1:
        config.update(Obstacle3, speed11)
        config.update(Obstacle4, speed12)
    if cp == 2:
        config.update(Obstacle3, speed21)
        config.update(Obstacle4, speed22)
    # if any player collects treasure, give them 20 points
    if (Player1.rect.x > 340 and Player1.rect.x < 380 and
        Player1.rect.y > 184 and Player1.rect.y < 224):
            if tc1 == 0:
                score1 += 20
                tc1 = 1
            Treasure.rect.x = 1000
            Treasure.rect.y = 1000
    if (Player2.rect.x > 340 and Player2.rect.x < 380 and
        Player2.rect.y > 184 and Player2.rect.y < 224):
            if tc2 == 0:
                score2 += 20
                tc2 = 1
            Treasure.rect.x = 1000
            Treasure.rect.y = 1000
    # on crossing fixed obstacles gain 5 pts
    # on crossing moving obstacles gain 10 pts
    if Player1.rect.bottom < 368:
        if x1 == 0:
            score1 += 10
            x1 = 1
    if Player1.rect.bottom < 276:
        if x2 == 0:
            score1 += 10
            x2 = 1
    if Player1.rect.bottom < 132:
        if x3 == 0:
            score1 += 10
            x3 = 1
    if Player1.rect.bottom < 40:
        if x4 == 0:
            score1 += 10
            x4 = 1
        cp = 2
        rnd = 1
        Player1.rect.x = 340
        Player1.rect.y = 469
        x1 = x2 = x3 = x4 = 0
    if Player2.rect.top > 408:
        if y1 == 0:
            score2 += 10
            y1 = 1
    if Player2.rect.top > 460:
        cp = 1
        rnd = 2
        Player2.rect.x = 340
        Player2.rect.y = 8
        y1 = y2 = y3 = y4 = 0
    if Player2.rect.top > 316:
        if y2 == 0:
            score2 += 10
            y2 = 1
    if Player2.rect.top > 184:
        if y3 == 0:
            score2 += 10
            y3 = 1
    if Player2.rect.top > 92:
        if y4 == 0:
            score2 += 10
            y4 = 1
    # check if player 1 has collided and died and display a message
    coll_list1 = pygame.sprite.spritecollide(Player1, obs_list, False)
    for i in coll_list1:
        death1 = 1
        message = font.render("PLAYER 1 HAS DIED!", True, config.black)
        textrect = message.get_rect()
        textrect.center = (350, 250)
        screen.blit(message, textrect)
        pygame.display.flip()
        pygame.time.delay(1000)
        cp = 2
        rnd = 1
        Player1.rect.x = 340
        Player1.rect.y = 469
        x1 = x2 = x3 = x4 = 0
    # check if player 2 has collided and died and display a message
    coll_list2 = pygame.sprite.spritecollide(Player2, obs_list, False)
    for i in coll_list2:
        death2 = 1
        message = font.render("PLAYER 2 HAS DIED!", True, config.black)
        textrect = message.get_rect()
        textrect.center = (350, 250)
        screen.blit(message, textrect)
        pygame.display.flip()
        pygame.time.delay(1000)
        cp = 1
        rnd = 2
        Player2.rect.x = 340
        Player2.rect.y = 0
        y1 = y2 = y3 = y4 = 0
    font = pygame.font.Font(config.font_name, 32)
    x = 0
    # if round 1 is done and treasure has not been collected, display treasure
    if rnd == 1 and tc2 == 0:
        Treasure.rect.x = 340
        Treasure.rect.y = 184
    # if round 2 is done, do the following
    if rnd == 2:
        tc1 = 0
        tc2 = 0
        if tc1 == 0:
            Treasure.rect.x = 340
            Treasure.rect.y = 184
        # go to next level
        level += 1
        if death1 == 1:
            if death2 == 1:
                x = 1
        # if both players died, decrement level, display no winner
        if x == 1:
            wp = 0
            level -= 1
            message = font.render("NO WINNER! :(", True, config.black)
            textrect = message.get_rect()
            textrect.center = (350, 300)
            screen.blit(message, textrect)
            pygame.display.flip()
            pygame.time.delay(1000)
        else:
            # if only player 2 died, player 1 won
            if death2 == 1:
                speed11 += 2
                speed12 += 2
                wp = 1
                message = font.render("PLAYER 1 WINS!", True, config.black)
                textrect = message.get_rect()
                textrect.center = (350, 300)
                screen.blit(message, textrect)
                pygame.display.flip()
                pygame.time.delay(1000)
            # if only player 1 died, player 2 won
            elif death1 == 1:
                speed21 += 2
                speed22 += 2
                wp = 2
                message = font.render("PLAYER 2 WINS!", True, config.black)
                textrect = message.get_rect()
                textrect.center = (350, 250)
                screen.blit(message, textrect)
                pygame.display.flip()
                pygame.time.delay(1000)
            elif score1 > score2:
                # playeryer 1 wins
                speed11 += 2
                speed12 += 2
                wp = 1
                message = font.render("PLAYER 1 WINS!", True, config.black)
                textrect = message.get_rect()
                textrect.center = (350, 250)
                screen.blit(message, textrect)
                pygame.display.flip()
                pygame.time.delay(1000)
            elif score1 < score2:
                # player2 wins
                speed21 += 2
                speed22 += 2
                wp = 2
                message = font.render("PLAYER 2 WINS!", True, config.black)
                textrect = message.get_rect()
                textrect.center = (350, 250)
                screen.blit(message, textrect)
                pygame.display.flip()
                pygame.time.delay(1000)
            elif score1 == score2:
                if time1 < time2:
                    # player1 wins
                    speed11 += 2
                    speed12 += 2
                    wp = 1
                    message = font.render("PLAYER 1 WINS!", True, config.black)
                    textrect = message.get_rect()
                    textrect.center = (350, 250)
                    screen.blit(message, textrect)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                else:
                    # player2 wins
                    speed21 += 2
                    speed22 += 2
                    wp = 2
                    message = font.render("PLAYER 2 WINS!", True, config.black)
                    textrect = message.get_rect()
                    textrect.center = (350, 250)
                    screen.blit(message, textrect)
                    pygame.display.flip()
                    pygame.time.delay(1000)
        # reinitialize scores, rounds and deaths to 0
        score1 = 0
        score2 = 0
        rnd = 0
        death1 = 0
        death2 = 0
        time1=0
        time2=0
    # draw all sprites onto screen
    all_sprites_list.draw(screen)
    # displaying scores, level, and current player on screen
    draw_text(screen, "PLAYER 1: " + str(score1), 24, 640, 465)
    draw_text(screen, "PLAYER 2: " + str(score2), 24, 60, 14)
    draw_text(screen, "PLAYER " + str(cp) + " IS PLAYING", 24, 620, 14)
    draw_text(screen, "LEVEL: " + str(level), 24, 49, 465)
    # below, we calculate time taken by player to reach other end
    if Player1.rect.bottom < 460:
        if Player1.rect.top > 40:
            time1 += 1
    if Player2.rect.bottom < 460:
        if Player2.rect.top > 40:
            time2 += 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
