# Imports
import sys
print(sys.path)
import pygame
from pygame.locals import *

# Global Static Variables
screen_width=720
screen_height=400
game_name = 'Game Name'


# Main function
# Where the magic happens
def main():
    # Init pygame, needed for modifications
    pygame.init()

    # Do a font and sound check
    # TODO: Add code to set font if not present
    if not pygame.font: print ('Warning, fonts disabled')
    if not pygame.mixer: print ('Warning, sound disabled')

    # Disable screensaver
    pygame.display.set_allow_screensaver(False)

    # Set the caption, the name that appears above the window
    pygame.display.set_caption(game_name)

    # Opens Display
    # Calls init if not inited
    # size is window size
    # depth is color depth, auto set to best settings if ignored
    window_surface = pygame.display.set_mode(size = [screen_width, screen_height])


    # Loop to play game
    running = True
    while running: 
        # Handle all queued events
        # If events are not used, they still need to be handled with pump()
        for event in pygame.event.get():
            # Game exit
            if event.type == QUIT:
                running = False

    # Close out pygame
    pygame.quit()

# Import protection
if __name__ == "__main__":
    sys.exit(main())