# Imports
import sys
print(sys.path)
import pygame
from pygame.locals import *

# Global Static Variables
screen_width=720
screen_height=400
game_name = 'PyGame Chess'
background_black =  (0, 0, 0)
board_black = (int("5B", 16), int("27", 16), int("0B", 16))
board_white = (int("DE", 16), int("B8", 16), int("87", 16))


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


        # Get the shape of the window (width, height)
        windowShape = pygame.display.get_window_size()

        # Set background color
        # Currently fills space with black
        window_surface.fill(background_black)

        # Get variables for board set up
        # Square size is how large the board squares are
        # Offset is used to center the board on the screen
        boardSquareSize = int(windowShape[1]/8)
        boardOffset = (int(windowShape[0])-boardSquareSize*8)/2

        # Draw the board
        for col in range(8):
            for row in range(8):
                boardRow = boardSquareSize * row + boardOffset
                boardCol = boardSquareSize * col
                # White squares
                if ((col + row) % 2 == 0):
                    pygame.draw.rect(window_surface, board_white, (boardRow, boardCol, boardSquareSize, boardSquareSize))
                # Black squares
                else:
                    pygame.draw.rect(window_surface, board_black, (boardRow, boardCol, boardSquareSize, boardSquareSize))

        # Draw frame to the screen
        pygame.display.flip()

    # Close out pygame
    pygame.quit()

# Import protection
if __name__ == "__main__":
    sys.exit(main())