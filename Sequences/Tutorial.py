from KeepingNasaAfloat.Classes.DialogueBoxes import *

import os

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
PALE_GREEN1 = (33, 222, 77)
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

Tutorial = create_tutorial_list()

# Set up background and display size

office = pygame.image.load(
            'KeepingNasaAfloat\\Sprites\\office.png')
office = pygame.transform.scale(office, (455, 683))
display = pygame.display.set_mode((455, 683))


# Set up buttons

YESbutton = TutorialYesNoButton(WHITE, 35, 540, 400, 50)
NObutton = TutorialYesNoButton(WHITE, 35, 600, 400, 50)


# Set up sounds

s = pygame.mixer.Sound("KeepingNasaAfloat\\Audio\\Typewriter click.wav")

# Set up icons

icons = [pygame.image.load("KeepingNasaAfloat\\Sprites\\USSR_meter_cutout.png"),
         pygame.image.load("KeepingNasaAfloat\\Sprites\\USA_meter_cutout.png"),
         pygame.image.load("KeepingNasaAfloat\\Sprites\\FLASK_cutout.png"),
         pygame.image.load("KeepingNasaAfloat\\Sprites\\SaturnV_cutout.png"),
         pygame.image.load("KeepingNasaAfloat\\Sprites\\DOLLAR_cutout.png"),
         pygame.image.load("KeepingNasaAfloat\\Sprites\\KUBRICK_cutout.png")]

icon_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\""Pokemon.ttf", 12)


""" 

Text Print

"""


def print_text(display, dialogue, i):

    """

    Prints dialogue text during interactive part of the game

    """

    text_pos = (50, 465)
    font_size = 24

    if i == 4:
        text_pos = (50, 460)
        font_size = 21
    if i == 2 or i == 3:
        text_pos = (50, 460)
        font_size = 20
    if i == 8 or i == 9 or i == 10 or i == 11 or i == 12:
        text_pos = (50, 460)
        font_size = 19

    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)

    words = dialogue[i][1].split(' ')

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


def print_character_description(Tutorial, i):

    text_pos = (35, 396)
    font_size = 23
    if i == 4:
        text_pos = (30, 396)
        font_size = 20
    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)

    words = Tutorial[i][4].split(' ')

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


def draw_YES_NO_buttons(Tutorial, i):

    YESbutton.draw(display, i, 5, True, ANTIQUE_WHITE, Tutorial[i][5])
    NObutton.draw(display, i, 6, False, ANTIQUE_WHITE, Tutorial[i][6])

    if i != 0:
        YESbutton.special_font_color = BLACK
        NObutton.special_font_color = BLACK


"""

GUIs

"""


def redraw_main_gui(character_dialogue, i):
    office.set_alpha(255 / 4 * i)
    display.blit(office, (0, 0))
    Dialogue1 = MainDialogueBox(display, (430, 215), (455, 683))
    Character_description_surf = Character_description_box(display, (430, 60), (455, 683))
    Point_indicator_surf = Point_indicator_box(display, (430, 80), (455, 683))
    print_character_description(Tutorial, i)
    print_text(display, Tutorial, i)


"""

Event reactions

"""


def on_event_tutorial(i):

    YESaction = False
    NOaction = False
    add_points = False
    in_tutorial = True

    for event in pygame.event.get():

        YESaction = False
        NOaction = False

        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if YESbutton.isOver(pos):
                empty_channel = pygame.mixer.find_channel()
                empty_channel.play(s)
                i = i + 1
                YESaction = True
                add_points = True
                break
            if NObutton.isOver(pos):
                empty_channel = pygame.mixer.find_channel()
                empty_channel.play(s)
                if i == 0:
                    in_tutorial = False
                    break
                i = i + 1
                NOaction = True
                add_points = True
                break

        if event.type == pygame.MOUSEMOTION:
            if YESbutton.isOver(pos):
                YESbutton.color = GREEN
                if i == 0:
                    YESbutton.special_font_color = WHITE
            else:
                YESbutton.color = WHITE
                if i == 0:
                    YESbutton.special_font_color = GREEN

            if NObutton.isOver(pos):
                NObutton.color = RED
                if i == 0:
                    NObutton.special_font_color = WHITE
            else:
                NObutton.color = WHITE
                if i == 0:
                    NObutton.special_font_color = RED

    return i, YESaction, NOaction, add_points, in_tutorial


"""

Point system

"""


def get_points(i, Tutorial, YESaction, NOaction):

    start_stats = True

    if YESaction:
        newpoints = Tutorial[i][2]
        start_stats = False
    elif NOaction:
        newpoints = Tutorial[i][3]
        start_stats = False
    else:
        newpoints = [0, 0, 0, 0, 0]

    return newpoints, start_stats


def update_points(score_up, score, newpoints, start_stats):

    if not start_stats:
        newpoints = [int(i) for i in newpoints.split(", ") if i.strip()]
    if score_up:
        for i in range(5):
            score[i] = score[i] + newpoints[i]
    return score


"""

Point indicators

"""


def draw_point_indicators(display, score, icons, icon_font):

    for a in range(5):

        column_height = score[a]/4
        if column_height < 0:
            column_height = 0

        column_space = pygame.Surface((40, 50))
        column_space.fill(BACKGROUND_BROWN)
        display.blit(column_space, (56 + 76 * a, 21.5))

        font = icon_font

        column = pygame.Surface((40, column_height))

        if a == 0:
            if score[a] <= 100:
                column = pygame.Surface((40, 50 - score[a] / 4))
                column.fill(SOVIET_RED)
                icon = pygame.transform.scale(icons[0], (40, 50))
                display.blit(column, (56 + 76 * a, 21.5 + score[a]/4))
                value = score[a]
                text = font.render(str(value), 1, SOVIET_RED)
            else:
                column.fill(NASA_BLUE)
                icon = pygame.transform.scale(icons[1], (40, 50))
                display.blit(column, (56 + 76 * a, 21.5 + (200 - score[a]) / 4))
                value = score[a]
                text = font.render(str(value), 1, NASA_BLUE)
        elif a == 1:
            column.fill(TURQUESA)
            icon = pygame.transform.scale(icons[2], (40, 50))
            display.blit(column, (56 + 76 * a, 21.5 + (200 - score[a]) / 4))
            value = score[a]
            text = font.render(str(value), 1, TURQUESA)
        elif a == 2:
            column.fill(NASA_BLUE)
            icon = pygame.transform.scale(icons[3], (40, 50))
            display.blit(column, (56 + 76 * a, 21.5 + (200 - score[a]) / 4))
            value = score[a]
            text = font.render(str(value), 1, NASA_BLUE)
        elif a == 3:
            column.fill(DOLLAR_GREEN)
            icon = pygame.transform.scale(icons[4], (40, 50))
            display.blit(column, (56 + 76 * a, 21.5 + (200 - score[a]) / 4))
            value = score[a]
            text = font.render(str(value), 1, DOLLAR_GREEN)
        elif a == 4:
            column.fill(BLACK)
            icon = pygame.transform.scale(icons[5], (40, 50))
            display.blit(column, (56 + 76 * a, 21.5 + (200 - score[a]) / 4))
            value = score[a]
            text = font.render(str(value), 1, BLACK)

        display.blit(icon, (56 + 76*a, 21.5))
        display.blit(text, (55.5 + 76.5 * a, 74))


"""

Main funtion

"""


def tutorial():

    pygame.mixer.music.load('KeepingNasaAfloat\\Audio\\Mixes\\Miles Davis, Lynyrd Skynyrd.wav')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(2)

    in_tutorial = True

    while in_tutorial:

        score = [100, 100, 100, 100, 100]
        YESaction = False
        NOaction = False
        add_points = False

        i = 0
        while i <= 13:
            if i < 5:
                redraw_main_gui(Tutorial[i][1], i)
                draw_YES_NO_buttons(Tutorial, i)
                print_text(display, Tutorial, i)
                i, YESaction, NOaction, add_points, in_tutorial = on_event_tutorial(i)
                if not in_tutorial:
                    break
            if not in_tutorial:
                break

            if i >= 5:
                if add_points:
                    newpoints, startstats = get_points(i-1, Tutorial, YESaction, NOaction)
                    update_points(add_points, score, newpoints, startstats)
                redraw_main_gui(Tutorial[i][1], i)
                draw_YES_NO_buttons(Tutorial, i)
                print_text(display, Tutorial, i)
                draw_point_indicators(display, score, icons, icon_font)
                i, YESaction, NOaction, add_points, in_tutorial = on_event_tutorial(i)
            if i == 14:
                in_tutorial = False

            pygame.display.update()

        pygame.mixer.music.fadeout(5000)

        for i in range(100):
            fade_surface = pygame.Surface((455, 683))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(255 * i / 1000)

            display.blit(fade_surface, (0, 0))

            pygame.display.update()
            pygame.time.delay(25)
