import os

from KeepingNasaAfloat.Sequences.Tutorial import tutorial
from KeepingNasaAfloat.Sequences.Easy_mode import easy_mode
from KeepingNasaAfloat.Sequences.Top_Scores import top_scores
from KeepingNasaAfloat.Sequences.Record_score import record_score
from KeepingNasaAfloat.Sequences.Intro import intro
from KeepingNasaAfloat.Sequences.Startscreen import Startscreen

from KeepingNasaAfloat.Animations.Simulation.GravSim import *
from KeepingNasaAfloat.Animations.Start import Intro_screen
from KeepingNasaAfloat.Animations.JFK_gameover import JFK
from KeepingNasaAfloat.Animations.Scientists_gameover import Scientists_class
from KeepingNasaAfloat.Animations.Engineers_gameover import Engineers
from KeepingNasaAfloat.Animations.Treasury_gameover import Money
from KeepingNasaAfloat.Animations.Kubrick_gameover import Stanley
from KeepingNasaAfloat.Animations.Win import Win

from KeepingNasaAfloat.End.Main import Stagrill

from KeepingNasaAfloat.Classes.DialogueBoxes import *

from KeepingNasaAfloat.Functions.KNA_functions import *

os.environ['SDL_VIDEO_CENTERED'] = '1'


"""


This is KEEPING NASA AFLOAT's main file!!!



The user, through an unexpected chain of events, has become president of NASA:

    As president of NASA, the user will receive a series of requests from:
    
        - JFK, President of the USA
        - Engineers
        - Scientists
        - and maybe Stanley Kubrick
    
    The choices made influence five indexes:
    
        - Cold-war-meter
        - Quality of spaceship parts
        - Scientific capability
        - Space program budget
        - and maybe money available to fake the landing/Kubrick's temper
    
    If any index reaches 0 or 200, the game ends with catastrophic consequences:
    
        - USSR wins/NASA becomes NAS-ICBM
        - Saturn V explodes on take-off/Engineers get cocky
        - Crash into the Moon due to bad calculations/Spaceship is forever lost due to too good calculations
        - Money runs out/Too much money makes for no good
        - and maybe the public discovers it was all a farce/Stan "machiavelli"s his way to the top of Nasa
    
    After 21 weeks (one choice = one week), granted NASA is still afloat, extra endgame material will kick in.


NOTE:
Importing the whole Classes and KeepingNasaAfloat_functions files means importing pygame,
sys, os would be redundant. That is why they are not here (but there).


IMPORTANT:
------------------------------------------------------------------------------------------------------------------------
|    MAIN DIRECTORY: C:\\Users\\xXY4n\\AE BSc\\AE Year 1\\Python\\GAME_pygame                              |
|                                                                                                                      |
|    Control+F to find every instance of it and change it accordingly to make the game usable in another machine.      |
|    This has to be done on every python file within the KeepingNasaAfloat directory (or not, but no guarantees then). |
------------------------------------------------------------------------------------------------------------------------

"""

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
size = (455, 683)
office = pygame.transform.scale(office, size)
display = pygame.display.set_mode(size)
pygame.display.set_caption('Keeping NASA afloat!')


# Set up buttons

YESbutton = YesNoButton(WHITE, 35, 540, 400, 50)
NObutton = YesNoButton(WHITE, 35, 600, 400, 50)

ENTERbutton = Button(WHITE, 27.5, 590, 400, 60)


# Set up screens and animations

Intro_surf = Intro_screen(display, size)


# Set up sounds

s = pygame.mixer.Sound("KeepingNasaAfloat\\Audio\\Typewriter click.wav")


""" 

Text Print

"""


def print_text(display, a, b, dialogue):

    """

    Prints dialogue text during interactive part of the game

    """

    text_pos = (50, 465)
    font_size = 24

    if (b, a) == (0, 1) or (b, a) == (0, 3) \
                        or (b, a) == (1, 0) or (b, a) == (1, 2) \
                        or (b, a) == (2, 0):
        text_pos = (50, 460)
        font_size = 23

    elif (b, a) == (0, 0) or (b, a) == (3, 3):
        font_size = (50, 460)
        font_size = 20

    elif (b, a) == (0, 2) or (b, a) == (2, 2):
        text_pos = (50, 462)
        font_size = (50, 460)
        font_size = 19

    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)

    words = dialogue[a][1].split(' ')

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


def print_character_description(character_dialogue, a):

    text_pos = (35, 396)
    font_size = 23
    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)

    words = character_dialogue[a][-4].split(' ')

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


def print_week(i):

    word_pos = (345, 110)
    word_font_size = 20
    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Cool Number Font\\Superstar M54.ttf", word_font_size)
    word = 'Week'
    word_surface = font.render(word, True, BLACK)
    display.blit(word_surface, word_pos)

    number_pos = (399, 127)
    number_font_size = 50
    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Cool Number Font\\Superstar M54.ttf", number_font_size)
    number = str(i)
    number_surface = font.render(number, True, WHITE)
    display.blit(number_surface, number_pos)

    number_pos = (397, 125)
    number_font_size = 50
    font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Cool Number Font\\Superstar M54.ttf", number_font_size)
    number = str(i)
    number_surface = font.render(number, True, BLACK)
    display.blit(number_surface, number_pos)


"""

Buttons

"""


def draw_YES_NO_buttons(character, a, b):
    YESbutton.draw(display, a, b, ANTIQUE_WHITE, character[a][-3])
    NObutton.draw(display, a, b, ANTIQUE_WHITE, character[a][-2])


"""

GUI

"""


def redraw_main_gui(character_dialogue, a, b, i):
    display.blit(office, (0, 0))
    Dialogue1 = MainDialogueBox(display, (430, 215), (455, 683))
    Character_description_surf = Character_description_box(display, (430, 60), (455, 683))
    Point_indicator_surf = Point_indicator_box(display, (430, 80), (455, 683))
    Week_indicator_surf = Week_indicator(display, (100, 50), (455, 683), i)
    print_character_description(character_dialogue, a)
    print_text(display, a, b, character_dialogue)
    print_week(i)


"""

Event reactions

"""


def on_event(i, newquestion):

    YESaction = False
    NOaction = False
    test = True

    while test:

        for event in pygame.event.get():

            YESaction = False
            NOaction = False

            pos = pygame.mouse.get_pos()

            newquestion = False

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if YESbutton.isOver(pos):
                    i = i + 1
                    newquestion = True
                    test = False
                    YESaction = True
                    empty_channel = pygame.mixer.find_channel()
                    empty_channel.play(s)
                    break

                if NObutton.isOver(pos):
                    i = i + 1
                    newquestion = True
                    test = False
                    NOaction = True
                    empty_channel = pygame.mixer.find_channel()
                    empty_channel.play(s)
                    break

    return i, newquestion, YESaction, NOaction


def on_scrolling_over_a_button():
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEMOTION:
            if YESbutton.isOver(pos):
                YESbutton.color = PALE_GREEN2
            else:
                YESbutton.color = WHITE

            if NObutton.isOver(pos):
                NObutton.color = RED
            else:
                NObutton.color = WHITE


"""

Point system

"""


def get_points(a, dialogue, YESaction, NOaction):

    start_stats = True

    if YESaction:
        newpoints = dialogue[a][2]
        start_stats = False
    elif NOaction:
        newpoints = dialogue[a][3]
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


def draw_point_indicators(display, score):

    for a in range(5):

        if score[a] < 0:
            score[a] = 0

        if score[a] > 200:
            score[a] = 200

        column_space = pygame.Surface((40, 50))
        column_space.fill(BACKGROUND_BROWN)
        display.blit(column_space, (56 + 76 * a, 21.5))

        column = pygame.Surface((40, score[a] / 4))

        icons = [pygame.image.load("KeepingNasaAfloat\\Sprites\\USSR_meter_cutout.png"),
                 pygame.image.load("KeepingNasaAfloat\\Sprites\\USA_meter_cutout.png"),
                 pygame.image.load("KeepingNasaAfloat\\Sprites\\FLASK_cutout.png"),
                 pygame.image.load("KeepingNasaAfloat\\Sprites\\SaturnV_cutout.png"),
                 pygame.image.load("KeepingNasaAfloat\\Sprites\\DOLLAR_cutout.png"),
                 pygame.image.load("KeepingNasaAfloat\\Sprites\\KUBRICK_cutout.png")]

        font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\""Pokemon.ttf", 12)

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

Endgame and main funtions

"""


def endgame(score, q):

    running = True
    win = False

    a = 0

    for i in range(5):
        if score[i] <= 0 or score[i] >= 200:
            a = i
            running = False
    if q > 20:
        running = False
        win = True

    branch = -1

    if not running:
        branch = a

    return running, win, branch


def main():
    i = 0
    a = 1
    b = 1
    newpoints = [0, 0, 0, 0, 0]
    score = [100, 100, 100, 100, 100]
    newquestion = True
    YESaction = False
    NOaction = False
    start_stats = True
    running = True
    win = False

    i = 0
    while running:

        score_up = False

        # Draw new question if there has been an answer, else draw previous
        if newquestion:

            # Update points
            newpoints, start_stats = get_points(a, Dialogue[b], YESaction, NOaction)

            previous_a = a
            previous_b = b
            finding_variable = True
            while finding_variable:
                new_a = dialogue_position()
                new_b = character_position()
                if previous_a != new_a or previous_b != new_b:
                    a = new_a
                    b = new_b
                    finding_variable = False

            score_up = True
        else:
            print_text(display, a, b, Dialogue[b])

        # Draw GUI
        redraw_main_gui(Dialogue[b], a, b, i)
        draw_YES_NO_buttons(Dialogue[b], a, b)

        score = update_points(score_up, score, newpoints, start_stats)
        draw_point_indicators(display, score)

        # Endgame function
        running, win, branch = endgame(score, i)

        if not running:
            break

        # Get new question index, booleans to new question, add or substract points
        pygame.display.update()

        i, newquestion, YESaction, NOaction = on_event(i, newquestion)

    pygame.mixer.music.fadeout(5000)

    for k in range(100):
        fade_surface = pygame.Surface((455, 683))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(255 * k / 1000)

        display.blit(fade_surface, (0, 0))

        pygame.display.update()
        pygame.time.delay(25)

    return i, branch, win, score


"""

Calls 

"""


Startscreen = Startscreen(display, size)


def run():
    Intro_surf.let_the_game_begin()
    path = Startscreen.on_event()
    Startscreen.roll_change()

    running = True

    while running:
        if path == 0:
            path = Startscreen.on_event(music=False)
            Startscreen.roll_change()
        if path == 1:
            Grav_Sim(display)
            tutorial()
            intro()
            weeks, branch, win, score = main()
            if not win:
                if branch == 0:
                    if score[0] >= 200:
                        End = JFK(True)
                        End.endgame()
                    else:
                        End = JFK(False)
                        End.endgame()
                elif branch == 1:
                    if score[1] >= 200:
                        End = Scientists_class(True)
                        End.endgame()
                    else:
                        End = Scientists_class(False)
                        End.endgame()
                elif branch == 2:
                    if score[2] >= 200:
                        End = Engineers(True)
                        End.endgame()
                    else:
                        End = Engineers(False)
                        End.endgame()
                elif branch == 3:
                    if score[3] >= 200:
                        End = Money(True)
                        End.endgame()
                    else:
                        End = Money(False)
                        End.endgame()
                elif branch == 4:
                    if score[4] >= 200:
                        End = Stanley(True)
                        End.endgame()
                    else:
                        End = Stanley(False)
                        End.endgame()
            else:
                if score[4] > (score[1]+score[2])*0.6:
                    End = Win(True)
                    End.endgame()
                    Stagrill(display)
                else:
                    End = Win(False)
                    End.endgame()
                    Stagrill(display)
            path = record_score(weeks)
        if path == 2:
            Grav_Sim(display)
            tutorial()
            intro()
            weeks, branch, win, score = easy_mode()
            if not win:
                if branch == 0:
                    if score[0] >= 200:
                        End = JFK(True)
                        End.endgame()
                    else:
                        End = JFK(False)
                        End.endgame()
                elif branch == 1:
                    if score[1] >= 200:
                        End = Scientists_class(True)
                        End.endgame()
                    else:
                        End = Scientists_class(False)
                        End.endgame()
                elif branch == 2:
                    if score[2] >= 200:
                        End = Engineers(True)
                        End.endgame()
                    else:
                        End = Engineers(False)
                        End.endgame()
                elif branch == 3:
                    if score[3] >= 200:
                        End = Money(True)
                        End.endgame()
                    else:
                        End = Money(False)
                        End.endgame()
                elif branch == 4:
                    if score[4] >= 200:
                        End = Stanley(True)
                        End.endgame()
                    else:
                        End = Stanley(False)
                        End.endgame()
            else:
                if score[4] > (score[1]+score[2])*0.6:
                    End = Win(True)
                    End.endgame()
                    Stagrill(display)
                else:
                    End = Win(False)
                    End.endgame()
                    Stagrill(display)
            path = record_score(weeks)
        if path == 3:
            top_scores()
            path = 0

    quit()
    sys.exit()


if __name__ == "__main__":
    run()
