import pygame
from KeepingNasaAfloat.Functions.KNA_functions import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ANTIQUE_WHITE = (139, 131, 120)
AZURE_4 = (131, 139, 139)
INDIAN_RED1 = (255, 106, 106)
PALE_GREEN2 = (144, 238, 144)
ORANGE4 = (139, 90, 0)
BLUE_GREY = (160, 165, 206)
NASA_BLUE = (30, 30, 255)
NASA_YELLOW = (255, 223, 91)
BACKGROUND_BROWN = (252, 244, 218)
SOVIET_RED = (179, 0, 0)
TURQUESA = (0, 255, 222)
DOLLAR_GREEN = (0, 128, 4)
UNREMARKABLE_GREY = (164, 164, 164)


class Button:

    """

    Button Class:
    This class allows for the creation of buttons with a rectangular (filleted) shape. A funtion is added to allow
    a change in color when the user scrolls over the button.
    Every other button class in this document is based on this one.

    """

    def __init__(self, color, x, y, width, height):
        """

        Initial constants

        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, outline=None, text=''):
        """

        Draws the button onto screen with or without outline and text.

        """
        self.text = text
        if outline:
            outline_rect = pygame.Rect(self.x + 3, self.y + 3, self.width + 1, self.height + 1)
            filled_rounded_rect(win, outline_rect, outline, 0.4)

        main_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        filled_rounded_rect(win, main_rect, self.color, 0.4)

        if self.text != '':
            font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", 25)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        """

        Evaluates if the mouse is on top of the button. Applied to change colors when scrolling over button.

        """
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class TopScoreScreenButton:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, outline=None, text='', console=None):
        self.text = text
        if outline:
            outline_rect = pygame.Rect(self.x + 3, self.y + 3, self.width + 1, self.height + 1)
            filled_rounded_rect(win, outline_rect, outline, 0.4)

        main_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        filled_rounded_rect(win, main_rect, self.color, 0.4)

        if self.text != '':
            """
            
            Text position, size and text line length are fine tuned to fit each button (Record Screen buttons vs
            "Write name in console" Screen button.
            Same thing happens when needed in the following classes.
            
            """

            word_spacing = 10
            text_line_space = 420
            font_size = 40
            if console:
                text_line_space = 400
                font_size = 50

            font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Brannboll\\BrannbollFS_PERSONAL.ttf", font_size)
            text = font.render(self.text, 1, (0, 0, 0))

            words = self.text.split(' ')

            x = self.x + (self.width / 2 - text.get_width() / 2)
            y = self.y + 2 + (self.height / 2 - text.get_height() / 2)
            if console:
                x = x+107
                y = y-20

            for word in words:
                word_surface = font.render(word, True, BLACK)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= text_line_space:
                    x = 100  # Reset the x.
                    y += word_height  # Start on new row.
                win.blit(word_surface, (x, y))
                x += word_width + word_spacing

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class EndgameScreenButton:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, outline=None, text='', a=None):
        self.text = text
        if outline:
            outline_rect = pygame.Rect(self.x + 3, self.y + 3, self.width + 1, self.height + 1)
            filled_rounded_rect(win, outline_rect, outline, 0.4)

        main_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        filled_rounded_rect(win, main_rect, self.color, 0.4)

        if self.text != '':
            font_size = 30
            b = 2
            if a:
                font_size = 50
                b = -5
            font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Brannboll\\BrannbollFS_PERSONAL.ttf", font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + b + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class StartButton:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, outline=None, text=''):
        self.text = text
        # Call this method to draw the button on the screen
        if outline:
            outline_rect = pygame.Rect(self.x + 3, self.y + 3, self.width + 1, self.height + 1)
            filled_rounded_rect(win, outline_rect, outline, 0.4)

        main_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        filled_rounded_rect(win, main_rect, self.color, 0.4)

        if self.text != '':
            font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", 30)
            text = font.render(self.text, 1, (30, 30, 30))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class YesNoButton:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, a, b, outline=None, text=''):
        self.text = text
        # Call this method to draw the button on the screen
        if outline:
            outline_rect = pygame.Rect(self.x + 3, self.y + 3, self.width + 1, self.height + 1)
            filled_rounded_rect(win, outline_rect, outline, 0.4)

        main_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        filled_rounded_rect(win, main_rect, self.color, 0.4)

        font_size = 25

        if (b, a, 4) == (0, 2, 4) or (b, a, 5) == (3, 2, 5) or (b, a, 5) == (3, 3, 5):
            font_size = 23

        if self.text != '':
            font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class TutorialYesNoButton:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.special_font_color = (0, 0, 0, 0)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, i, b, TrueorFalse, outline=None, text=''):
        self.text = text
        # Call this method to draw the button on the screen
        if outline:
            outline_rect = pygame.Rect(self.x + 3, self.y + 3, self.width + 1, self.height + 1)
            filled_rounded_rect(win, outline_rect, outline, 0.4)

        main_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        filled_rounded_rect(win, main_rect, self.color, 0.4)

        font_color = BLACK
        font_size = 25

        if (i, b) == (2, 5) or (i, b) == (2, 6) or (i, b) == (8, 6) or (i, b) == (9, 6):
            font_size = 20
        if (i, b) == (6, 5) or (i, b) == (6, 6):
            font_size = 18

        font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)

        if i == 0:
            font_size = 55
            font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Remachine\\RemachineScript_PERSONAL_USE_ONLY.ttf", font_size)
            if TrueorFalse:
                font_color = GREEN
            else:
                font_color = RED

        if self.special_font_color != (0, 0, 0, 0):
            font_color = self.special_font_color

        if self.text != '':
            text = font.render(self.text, 1, font_color)
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False
