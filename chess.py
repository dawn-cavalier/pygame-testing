# Imports
import sys
print(sys.path)
import pygame
from pygame.locals import *

# Global Static Variables
screen_width=720
screen_height=400
game_name = 'PyGame Chess'


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
    # This needs to be done before any events can be handle
    # size is window size
    # depth is color depth, auto set to best settings. Leave it ignored
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

        # Set background color
        # Currently fills space with black
        window_surface.fill((0, 0, 0))

        # Draw a rectangle
        # Set to color red
        # Draws a rectangle at (395, 0) with dimensions (10,10)
        pygame.draw.rect(window_surface, (255, 0, 0), (395,0,10,10))

        # Draw frame to screens
        pygame.display.flip()

    # Close out pygame
    pygame.quit()

# Import protection
if __name__ == "__main__":
    sys.exit(main())