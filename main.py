# This file was created by: Angel Zermeno

# Sources 
# LeMaster Tech https://www.youtube.com/watch?v=9H27CimgPsQ
# Mr.Cozort source code
# https://code.visualstudio.com/docs/getstarted/tips-and-tricks
# LeMaster Tech https://www.youtube.com/watch?v=hsJ7K301mEU
# World of Python https://www.youtube.com/watch?v=5-WGGYLT8E8


# Goals
# Create the pop up screen
# Add player and mob 
# Figure out how to make the player die when it hits a mob 
# Add platforms where the characters have to move around and avoid 

# content from kids can code: http://kidscancode.org/blog/
# import libraries and modules
# Content from github https://gist.github.com/erfansahaf/9aecee1c13887e6151c54425082e6444


#GOALS
#Don't get hit by the moving platform 
#Move up the screen
#Get the game over screen

import pygame
import sys
import random
import os


# setup asset folders here - images sounds etc. (This did not work)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

def new(self):
    self.bgimage = pygame.image.load(os.path.join(img_folder, 'space.jpg')).cnovert()

# Initialize Pygame (Game start up)
pygame.init()
WIDTH,LENGTH = 800,600
screen = pygame.display.set_mode((WIDTH,LENGTH))

# Load background image (big stuggle)
background_image = pygame.image.load(os.path.join(img_folder, 'space.jpg')).convert()
background_image = pygame.transform.scale(background_image, (0,0))

# Game settings (Learrning how to make the game demensions is something I used from our very first game which was rock paper scisores)
WIDTH, HEIGHT = 600, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player Settings (Understanding the perfect size so the player has the best success rate)
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy Settings (This is the same as the players settings just this one had a single path of motion)
enemy_size = 50
enemy_speed = 5
enemy_frequency = 25
enemies = []

# Create the game window (How the play screen shows up) (Learned from the mario game we made in class)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Game")
clock = pygame.time.Clock()

# How the player and enemy move
# Playe will move around on the x and y axis depending on where you choose
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])
# The enemy player has a constant downward motion on the y axis
def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, [x, y, enemy_size, enemy_size])

# What is shown at the end of the game with text 
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("You Suck try again", True, WHITE)
    screen.blit(text, (WIDTH // 5, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000) # How long you see the screen for before it closes
    pygame.quit()
    sys.exit() # How the screen closes

# How to make the player and mobs fucntion 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player around the screen 
    # This was the most difficult part of the whole code 
    # I DO NOT CLAIM THIS PART OF THE CODE I learned it from LeMasterTech
    # This part belongs to LeMasterTech https://www.youtube.com/watch?v=hsJ7K301mEU
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Create enemies (Falling down the screen)
    if random.randint(1, enemy_frequency) == 1:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # Move enemies (Down the screen)
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Check for collisions with enemies 
    # LeMasterTech Taught me how to do this in in pac man video
    for enemy in enemies:
        if (
            player_x < enemy[0] + enemy_size
            and player_x + player_size > enemy[0]
            and player_y < enemy[1] + enemy_size
            and player_y + player_size > enemy[1]
        ):
            game_over()

    # Remove off-screen enemies (Learned this from the mario game we made in class where the character fazed throught he screen)
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]

    # Draw the background
    screen.fill((0, 0, 0))

    # Draw the player
    draw_player(player_x, player_y)

    # Draw the enemies
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    # Update the display (Once game is over)
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)

