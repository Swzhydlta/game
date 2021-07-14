# This is a simple game program built using the pygame library.
# The user controls a sprite which has to dodge enemies
# and get from the left to the right side of the screen to win.

import pygame
import random 

# Initialize the pygame modules to get everything started.

pygame.init() 

# Set width and height of screen.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) 

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("playerG.png")
enemy1 = pygame.image.load("monster1.jpg")
enemy2 = pygame.image.load("monster2.jpg")
enemy3 = pygame.image.load("monster3.jpg")
prize = pygame.image.load("prizeMe.png")


# Get the width and height of the images in order to do boundary detection. 

image_height = player.get_height()
image_width = player.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player, enemy, and prize as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemies start off screen and at a random y position.

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)
prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up, down, left, or right keys are pressed.
# Right now they are not so make them equal False. 

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop which refreshes/updates the screen window
# and applies changes to represent real time game play. 

while 1: 

    screen.fill(0) # This clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition)) # This draws the player image to the screen at the postion specified.
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip() # This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user presses a key.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
                
        # This event checks if the key is up (i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 2
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 2
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerXPosition -= 2
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 2
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box and update enemyBox for the enemies:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box and update prizeBox for prize:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quit game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    
    if enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width:
    
        # Display winning status to the user: 
        
        print("You win!")
        
        # Quit game and exit window:
        
        pygame.quit()
        
        exit(0)

    # If the player collides with the prize, they win the game:
        
    if playerBox.colliderect(prizeBox):
        
        # Display winning status to the user: 
        
        print("You win!")
        
        # Quit game and exit window:
        
        pygame.quit()
        
        exit(0)
    
    # Make enemy approach the player.
    
    enemy1XPosition -= 0.50
    enemy2XPosition -= 0.50
    enemy3XPosition -= 0.50

    # Make prize approach the player.

    prizeXPosition -= 0.50


    
    # ================The game loop logic ends here. =============
  
