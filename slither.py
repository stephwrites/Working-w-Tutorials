import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

# actual game display and game name in top bar
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

block_size = 10
fps = 30

# object for function message_to_screen
# font and font size (25)
font = pygame.font.SysFont(None,25)

# function to print a message to the screen
def message_to_screen(msg,color):
    # render the font
    screen_text = font.render(msg,True,color)
    # puts font to screen
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    
def gameLoop():
    gameExit = False
    gameOver = False

    # snake starting point 
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    rand_apple_x = random.randrange(0,display_width - block_size)
    rand_apple_y = random.randrange(0,display_height - block_size)
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over" + '\n' + "Press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            # START EVENTS
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True

            # move forward/backwords by holding key
            #if event.type == pygame.KEYUP:
             #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              #      lead_x_change = 0
                    

            # END EVENTS
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        # (x, y, [width, height])
        pygame.draw.rect(gameDisplay,red,[rand_apple_x,rand_apple_y,block_size,block_size])
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
        
        pygame.display.update()

        clock.tick(fps)

        # END EVENTS

    # unitializes things initialized
    pygame.quit()
    # exits python
    quit()

gameLoop()
