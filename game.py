import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))

done = False

backgroundImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/background.jpg')
h3Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h3.png')
h2Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h2.png')
h1Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h1.png')
h0Image = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/h0.png')
winImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/win1.png')
gameoverImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/game-over.png')


#Player
playerImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/player.png')
player_x = 200
player_y = 500
def player(x, y):
    screen.blit(playerImage, (x, y))

#Enemy
enemyImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/enemy.png')
enemy_x = random.randint(0, 535)
enemy_y = 10
def enemy(x, y):
    screen.blit(enemyImage, (x, y))
enemy_dx = 2
enemy_dy = 50

#Bullet
bulletImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/bullet.png')
bullet_x = 0
bullet_y = 500
bullet_dy = 10
bullet_state = "ready"  

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x+10, y-25))

def isCollided(enemy_x, enemy_y, bullet_x, bullet_y):
    #distance
    d = math.sqrt((math.pow(enemy_x - bullet_x,2)) + (math.pow(enemy_y - bullet_y,2)))
    if d < 27 :
        return True
    else:
        return False

def isCollided2(enemy_x, enemy_y, player_x, player_y):
    #distance
    d = math.sqrt((math.pow(enemy_x - player_x,2)) + (math.pow(enemy_y - player_y,2)))
    if d < 64 :
        return True
    else:
        return False

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)

score_x = 450
score_y = 10

def playerScore(x, y):
    score = font.render("SCORE " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def heart(score_value):
    screen.blit(h3Image, (0, 0))
    if score_value >= 3:
        screen.blit(h2Image, (0, 0))
    if score_value >= 6:
        screen.blit(h1Image, (0, 0))
    if score_value >= 9:
        screen.blit(h0Image, (0, 0))
        screen.blit(winImage, (172, 172))
        

while not done:
    for event in pygame.event.get():
        #event on quit
        if event.type == pygame.QUIT:
            done = True     
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: player_x -= 3
    if pressed[pygame.K_RIGHT]: player_x += 3
    if pressed[pygame.K_UP]:
        if bullet_state == "ready":
            bullet_x = player_x
            fire_bullet(bullet_x, bullet_y)

    screen.fill((0, 0, 0))

    screen.blit(backgroundImage, (0, 0))

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    heart(score_value)
    playerScore(score_x, score_y)

    #Enemy moves
    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x >536:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy

    
    #Bullet moves
    if bullet_y<=0:
        bullet_y = 475
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_dy
    
    #collision between enemy and bullet
    coll = isCollided(enemy_x, enemy_y, bullet_x, bullet_y)
    if coll:
        bullet_y = 475
        bullet_state = "ready"
        score_value += 1
        if score_value is 9:
            enemy_dx = 0
            enemy_dy = 0

    #collision between enemy and player
    coll2 = isCollided2(enemy_x, enemy_y, player_x, player_y)
    if coll2:
        enemy_dx = 0
        enemy_dy = 0
        screen.blit(gameoverImage, (172, 172))

    if coll and coll2:
        coll is False
        screen.blit(gameoverImage, (172, 172))

    pygame.display.flip()