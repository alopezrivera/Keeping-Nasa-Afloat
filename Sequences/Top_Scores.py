from KeepingNasaAfloat.Classes.DialogueBoxes import *
from KeepingNasaAfloat.Functions.KNA_functions import *

import os


os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.font.init()

# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT_WHITE = (255, 255, 255, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ANTIQUE_WHITE = (139, 131, 120)
TRANSPARENT_ANTIQUE_WHITE = (139, 131, 120, 0)
AZURE_4 = (131, 139, 139)
INDIAN_RED1 = (255, 106, 106)
PALE_GREEN2 = (144, 238, 144)
ORANGE4 = (139, 90, 0)
BLUE_GREY = (160, 165, 206)
NASA_BLUE = (62, 75, 255)
TRANSPARENT_NASA_BLUE = (62, 75, 255, 240)
BACKGROUND_BROWN = (252, 244, 218)
SOVIET_RED = (179, 0, 0)
TURQUESA = (0, 255, 222)
DOLLAR_GREEN = (0, 128, 4)
UNREMARKABLE_GREY = (164, 164, 164)

# Set up background and display size

background = pygame.image.load('KeepingNasaAfloat\\Sprites\\Top_scores_background.jpg')
size = background.get_rect().size
display = pygame.display.set_mode(size)


# Set up buttons

BACK_TO_MENU_button = TopScoreScreenButton(TRANSPARENT_WHITE, 55, 570, 350, 80)

# Set up sounds

s = pygame.mixer.Sound("KeepingNasaAfloat\\Audio\\Typewriter click.wav")


""" 

Text Print

"""


def print_top_scores(display):

    """

    Prints dialogue in top score screen

    """

    # Set up dialogue

    Top_Scores = create_top_scores_list()

    # Set up font for introduction of the game
    number_font_size = 18
    number_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", number_font_size)
    username_font_size = 18
    username_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", username_font_size)
    dots_font_size = 20
    dots_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", dots_font_size)
    points_font_size = 18
    points_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", points_font_size)

    a = 60

    for i in range(10):

        for j in range(4):

            if j == 0:

                number_pos = (55, a + 48*i)
                number = Top_Scores[i][j]

                x_number = number_pos[0]
                y_number = number_pos[1]

                word_surface = number_font.render(number, True, BLACK)
                display.blit(word_surface, (x_number, y_number))

            if j == 1:

                username_pos = (90, a + 48*i)
                username = Top_Scores[i][j]

                x_user = username_pos[0]
                y_user = username_pos[1]

                word_surface = username_font.render(username, True, BLACK)
                display.blit(word_surface, (x_user, y_user))

            if j == 2:

                if i == 0:
                    extra = 3
                else:
                    extra = 0

                dots_pos = (175 + extra, a + 48*i - 1)
                dots = Top_Scores[i][j]

                x_dots = dots_pos[0]
                y_dots = dots_pos[1]

                word_surface = dots_font.render(dots, True, BLACK)
                display.blit(word_surface, (x_dots, y_dots))

            if j == 3:

                points_pos = (325, a + 48*i)
                points = Top_Scores[i][j]

                x_points = points_pos[0]
                y_points = points_pos[1]

                word_surface = points_font.render(points, True, BLACK)
                display.blit(word_surface, (x_points, y_points))


"""

Buttons

"""


def draw_BACK_TO_MENU_button():
    BACK_TO_MENU_button.draw(display, TRANSPARENT_ANTIQUE_WHITE, 'Back to menu')


"""

GUIs

"""


def redraw_intro_gui():
    display.blit(background, (0, 0))
    Dialogue1 = Top_scores_description_box(display, (380, 500), (455, 683))


"""

Event reactions

"""


def on_event_top_scores():

    in_top_score_screen = True

    for event in pygame.event.get():

        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if BACK_TO_MENU_button.isOver(pos):
                in_top_score_screen = False
                empty_channel = pygame.mixer.find_channel()
                empty_channel.play(s)
        if event.type == pygame.MOUSEMOTION:
            if BACK_TO_MENU_button.isOver(pos):
                BACK_TO_MENU_button.color = TRANSPARENT_NASA_BLUE
            else:
                BACK_TO_MENU_button.color = TRANSPARENT_WHITE
    return in_top_score_screen


"""

Top scores

"""


def top_scores():

    pygame.mixer.music.load("KeepingNasaAfloat\\Audio\\Frank Sinatra - Fly Me To The Moon.wav")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    in_top_score_screen = True
    i = 0
    while in_top_score_screen:
        redraw_intro_gui()
        draw_BACK_TO_MENU_button()
        print_top_scores(display)
        pygame.display.update()
        in_top_score_screen = on_event_top_scores()

    pygame.mixer.music.fadeout(5000)

    for i in range(100):
        fade_surface = pygame.Surface((455, 683))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(255 * i / 1000)

        display.blit(fade_surface, (0, 0))

        pygame.display.update()
        pygame.time.delay(25)

