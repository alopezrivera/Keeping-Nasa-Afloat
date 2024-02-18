import os
import pygame

from KeepingNasaAfloat.Sequences.Tutorial import *
from KeepingNasaAfloat.Functions.KNA_functions import *


os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.font.init()

# Colors

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
NASA_BLUE = (62, 75, 255)
BACKGROUND_BROWN = (252, 244, 218)
SOVIET_RED = (179, 0, 0)
TURQUESA = (0, 255, 222)
DOLLAR_GREEN = (0, 128, 4)
UNREMARKABLE_GREY = (164, 164, 164)

# Set up dialogue

President = create_dialogue_lists()[0]
Suppliers = create_dialogue_lists()[1]
Scientists = create_dialogue_lists()[2]
SK = create_dialogue_lists()[3]
Intro = create_dialogue_lists()[4]

Dialogue = [President, Suppliers, Scientists, SK]

# Set up background and display size

office = pygame.image.load(
            'KeepingNasaAfloat\\Sprites\\office.png')
size = office.get_rect().size
display = pygame.display.set_mode(size)


# Set up buttons

ENTERbutton = Button(WHITE, 27.5, 590, 400, 60)

# Set up sounds

s = pygame.mixer.Sound("KeepingNasaAfloat\\Audio\\Typewriter click.wav")


""" 

Text Print

"""


def print_intro_text(display, i):

    """

    Prints dialogue text during introduction to the game

    """

    text_pos = (45, 470)

    # Set up font for introduction of the game
    if i == 0:
        font_size = 40
        text_pos = (50, 475)
    elif i == 6:
        font_size = 22
        text_pos = (50, 467)
    else:
        font_size = 25

    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\"
                            "atwriter.ttf", font_size)

    # Set up secondary font
    font_size2 = 10
    font2 = pygame.font.Font("KeepingNasaAfloat\\Fonts\\"
                             "atwriter.ttf", font_size2)

    words = Intro[i][1].split(' ')

    word_spacing = 10
    text_line_space = 420
    x = text_pos[0]
    y = text_pos[1]

    for word in words:
        word_surface = font.render(word, True, BLACK)
        word_width, word_height = word_surface.get_size()
        if x + word_width >= text_line_space:
            x = text_pos[0]   # Reset the x.
            y += word_height  # Start on new row.
        display.blit(word_surface, (x, y))
        x += word_width + word_spacing

    # word_surface2 = font2.render('Press Enter to exit tutorial', True, BLACK)
    # display.blit(word_surface2, (text_pos[0], text_pos[1] + 100))


def print_intro_character_description():

    text_pos = (35, 390)
    font_size = 23
    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\"
                            "atwriter.ttf", font_size)

    words = 'John Fitzgerald Kennedy'.split(' ')

    word_spacing = 10
    text_line_space = 420
    x = text_pos[0]
    y = text_pos[1]

    for word in words:
        word_surface = font.render(word, True, BLACK)
        word_width, word_height = word_surface.get_size()
        if x + word_width >= text_line_space:
            x = text_pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        display.blit(word_surface, (x, y))
        x += word_width + word_spacing


"""

Buttons

"""


def draw_ENTER_button(i):
    ENTERbutton.draw(display, ANTIQUE_WHITE, Intro[i][-2])


"""

GUIs

"""


def redraw_intro_gui(i):
    Character_description_intro_surf = Intro_description_box(display, (430, 60), (455, 683))
    print_intro_character_description()
    Dialogue1 = IntroDialogueBox(display, (430, 220), (455, 683))


"""

Event reactions

"""


def on_event_intro(i):

    for event in pygame.event.get():

        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ENTERbutton.isOver(pos):
                i = i + 1
                empty_channel = pygame.mixer.find_channel()
                empty_channel.play(s)
        if event.type == pygame.MOUSEMOTION:
            if ENTERbutton.isOver(pos):
                ENTERbutton.color = GREEN
            else:
                ENTERbutton.color = WHITE
    return i


def intro():
    pygame.mixer.music.load('KeepingNasaAfloat\\Audio\\Mixes\\Zimmer, Bowie, Elton Britt, Ruben Blades.wav')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    i = 0
    while i < 7:
        redraw_intro_gui(i)
        draw_ENTER_button(i)
        print_intro_text(display, i)
        pygame.display.update()
        i = on_event_intro(i)

    for i in range(100):
        fade_surface = pygame.Surface((455, 683))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(255 * i / 1000)

        display.blit(fade_surface, (0, 0))

        pygame.display.update()
        pygame.time.delay(25)


