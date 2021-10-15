import pygame
import random

# Initialize the pygame.
pygame.init()

# Create the screen.
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Space War - A Game by Ram Kumar")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spacecraft.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        # Setting no movement of warship after key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    # Warship movement to left or right.
    playerX += playerX_change

    # Boundaries to player (warship) movement
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Boundaries to player (warship) movement


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

pygame.quit()
