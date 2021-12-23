# Imports
import sys
print(sys.path)
import pygame
from pygame.locals import *

from utils.spritesheet import SpriteSheet

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
        self.windowSurface = pygame.display.set_mode(size = [self.screen_width, self.screen_height])

        # Load pieces
        self.chessSet = ChessPieces(self, "images/chess_pieces.bmp")


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

        ## Set background color
        self.windowSurface.fill(self.background_black)
        
        ## Draw the board
        # Get variables for board set up
        boardSquareSize = int(windowShape[1]/8)
        if (boardSquareSize*8 > windowShape[0]):
            boardSquareSize = int(windowShape[0]/8)

        boardHorizontalOffset = int((windowShape[0]-boardSquareSize*8)/2)
        boardVerticalOffset = int((windowShape[1]-boardSquareSize*8)/2)

        # Drawing the board
        for col in range(8):
            for row in range(8):
                boardRow = boardSquareSize * row + boardHorizontalOffset
                boardCol = boardSquareSize * col + boardVerticalOffset
                boardLocation = pygame.Rect(boardRow, boardCol, boardSquareSize, boardSquareSize)
                # White squares
                if ((col + row) % 2 == 0):
                    pygame.draw.rect(self.windowSurface, self.board_white, boardLocation)
                # Black squares
                else:
                    pygame.draw.rect(self.windowSurface, self.board_black, boardLocation)

        ## Draw the peices
        # Draw black pieces
        for piece in self.chessSet.pieces[:6]:
            piece.blitme(boardSquareSize)

        # Draw white pieces
        for piece in self.chessSet.pieces[6:]:
            piece.blitme(boardSquareSize)
        # Draw frame to the screen
        pygame.display.flip()

class ChessPiece:
    def __init__(self, chessGame):
        # Initialize attributes to represent a chess piece.
        self.image = None
        self.name = ''
        self.color = ''

        self.windowSurface = chessGame.windowSurface

        # Start each peice on top left tile
        self.x, self.y = 0, 0

    def blitme(self, boardSquareSize):
        # Draw the piece at its current location
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x * boardSquareSize, self.y * boardSquareSize
        self.windowSurface.blit(self.image, self.rect)

class ChessPieces:
    def __init__(self, chessGame, spriteSheetFilename):
        self.chessGame = chessGame
        self.pieces = []

        self._load_pieces(spriteSheetFilename)


    def _load_pieces(self, spriteSheetFilename):
        spriteSheet = SpriteSheet(spriteSheetFilename)

        # Load images
        piece_images = spriteSheet.load_grid_images(2, 6, x_margin=64,
                x_padding=72, y_margin=68, y_padding=48)

        # Create a Piece for each image.
        colors = ['black', 'white']
        names = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

        pieceNum = 0
        for color in colors:
            for name in names:

                if name != 'pawn':
                    if color == 'black':
                        board_y = 0
                    else:
                        board_y = 7
                else:
                    if color == 'black':
                        board_y = 1
                    else:
                        board_y = 6


                match name:
                    case 'king':
                        self.pieces.append(self._create_piece(name, color, piece_images[pieceNum], 4, board_y))
                    case 'queen':
                        self.pieces.append(self._create_piece(name, color, piece_images[pieceNum], 3, board_y))
                    case 'rook':
                        for i in range(2):
                            self.pieces.append(self._create_piece(name, color, piece_images[pieceNum], 7*i, board_y))
                    case 'bishop':
                        for i in range(2):
                            self.pieces.append(self._create_piece(name, color, piece_images[pieceNum], 3*i+2, board_y))
                    case 'knight':
                        for i in range(2):
                            self.pieces.append(self._create_piece(name, color, piece_images[pieceNum], 5*i+1, board_y))
                    case 'pawn':
                        for i in range(8):
                            self.pieces.append(self._create_piece(name, color, piece_images[pieceNum], i, board_y))

                pieceNum += 1

    def _create_piece(self, name, color, image, x, y):
        piece = ChessPiece(self.chessGame)
        piece.name = name
        piece.color = color
        piece.image = image
        
        piece.x = x
        piece.y = y
        
        return piece
                            
        

def main():
    chessGame = ChessGame()
    chessGame.run()


# Import protection
if __name__ == "__main__":
    sys.exit(main())