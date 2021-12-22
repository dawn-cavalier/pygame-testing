# Imports
import sys
print(sys.path)
import pygame
from pygame.locals import *

class ChessGame:
    def __init__(self):
        # Declare all internal veraibles
        self.screen_width=720
        self.screen_height=400
        self.game_name = 'PyGame Chess'
        self.background_black =  (0, 0, 0)
        self.board_black = (int("5B", 16), int("27", 16), int("0B", 16))
        self.board_white = (int("DE", 16), int("B8", 16), int("87", 16))

        # Init pygame, needed for modifications
        pygame.init()

        # Do a font and sound check
        if not pygame.font: print ('Warning, fonts disabled')
        if not pygame.mixer: print ('Warning, sound disabled')

        # Disable screensaver
        pygame.display.set_allow_screensaver(False)

        # Set the caption, the name that appears above the window
        pygame.display.set_caption(self.game_name)

        # Opens Display
        # Calls init if not inited
        # This needs to be done before any events can be handle
        # size is window size
        # depth is color depth, auto set to best settings. Leave it ignored
        self.window_surface = pygame.display.set_mode(size = [self.screen_width, self.screen_height])

    def run(self):
        while(True):
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            # Game exits
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                

    def _update_screen(self):
        # Get the shape of the window (width, height)
        windowShape = pygame.display.get_window_size()

        # Set background color
        # Currently fills space with black
        self.window_surface.fill(self.background_black)

        # Get variables for board set up
        boardSquareSize = int(windowShape[1]/8)
        if (boardSquareSize*8 > windowShape[0]):
            boardSquareSize = int(windowShape[0]/8)

        boardHorizontalOffset = int((windowShape[0]-boardSquareSize*8)/2)
        boardVerticalOffset = int((windowShape[1]-boardSquareSize*8)/2)

        # Draw the board
        for col in range(8):
            for row in range(8):
                boardRow = boardSquareSize * row + boardHorizontalOffset
                boardCol = boardSquareSize * col + boardVerticalOffset
                # White squares
                if ((col + row) % 2 == 0):
                    pygame.draw.rect(self.window_surface, self.board_white, (boardRow, boardCol, boardSquareSize, boardSquareSize))
                # Black squares
                else:
                    pygame.draw.rect(self.window_surface, self.board_black, (boardRow, boardCol, boardSquareSize, boardSquareSize))

        # Draw frame to the screen
        pygame.display.flip()

def main():
    chessGame = ChessGame()
    chessGame.run()


# Import protection
if __name__ == "__main__":
    sys.exit(main())