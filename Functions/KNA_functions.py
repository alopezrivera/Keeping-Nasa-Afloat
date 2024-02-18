from pygame import *
import random


def open_file_and_write_to_table(file):

    qfile = open(file, 'r')
    lines = qfile.readlines()
    qfile.close()

    table = []

    for line in lines:
        if len(line.strip()) > 0:
            table.append(line.split('] -- ['))
    return table


def create_dialogue_lists_letter_by_letter():

    Inpath = r'KeepingNasaAfloat\Dialogue\Intro.dat'
    Intro = open_file_and_write_to_table(Inpath)

    i = 0
    intro_letters = []

    while i <= len(Intro) - 1:
        intro_letters.append(list(Intro[i][1]))
        i = i + 1

    Prpath = r'KeepingNasaAfloat\Dialogue\President.dat'
    President = open_file_and_write_to_table(Prpath)

    i = 0
    president_letters = []

    while i <= len(President) - 1:
        president_letters.append(list(President[i][1]))
        i = i + 1

    Sppath = r'KeepingNasaAfloat\Dialogue\Engineers.dat'
    Suppliers = open_file_and_write_to_table(Sppath)

    i = 0
    suppliers_letters = []

    while i <= len(Suppliers) - 1:
        intro_letters.append(list(Suppliers[i][1]))
        i = i + 1

    Scpath = r'KeepingNasaAfloat\Dialogue\ScientistsEndgame.dat'
    Scientists = open_file_and_write_to_table(Scpath)

    i = 0
    scientists_letters = []

    while i <= len(Scientists) - 1:
        scientists_letters.append(list(Scientists[i][1]))
        i = i + 1

    SKpath = r'KeepingNasaAfloat\Dialogue\SK.dat'
    SK = open_file_and_write_to_table(SKpath)

    i = 0
    sk_letters = []

    while i <= len(SK)-1:
        sk_letters.append(list(SK[i][1]))
        i = i + 1

    return president_letters, suppliers_letters, scientists_letters, sk_letters, intro_letters


def create_dialogue_lists():

    Inpath = r'KeepingNasaAfloat\Dialogue\Intro.dat'
    Intro = open_file_and_write_to_table(Inpath)

    Prpath = r'KeepingNasaAfloat\Dialogue\President.dat'
    President = open_file_and_write_to_table(Prpath)

    Sppath = r'KeepingNasaAfloat\Dialogue\Engineers.dat'
    Suppliers = open_file_and_write_to_table(Sppath)

    Scpath = r'KeepingNasaAfloat\Dialogue\Scientists.dat'
    Scientists = open_file_and_write_to_table(Scpath)

    SKpath = r'KeepingNasaAfloat\Dialogue\SK.dat'
    SK = open_file_and_write_to_table(SKpath)

    return President, Suppliers, Scientists, SK, Intro


def create_tutorial_list():
    Tutpath = r'KeepingNasaAfloat\Dialogue\Tutorial.dat'
    Tutorial = open_file_and_write_to_table(Tutpath)

    return Tutorial


def create_top_scores_list():
    Top_Scores_path = r'KeepingNasaAfloat\Dialogue\Top_Scores.dat'
    Top_Scores = open_file_and_write_to_table(Top_Scores_path)

    return Top_Scores


def create_endgame_list(a):
    Tutpath = [r'KeepingNasaAfloat\Dialogue\Endgames\JFKEndgame.dat',
               r'KeepingNasaAfloat\Dialogue\Endgames\ScientistsEndgame.dat',
               r'KeepingNasaAfloat\Dialogue\Endgames\EngineersEndgame.dat',
               r'KeepingNasaAfloat\Dialogue\Endgames\MoneyEndgame.dat',
               r'KeepingNasaAfloat\Dialogue\Endgames\StanleyEndgame.dat',
               r'KeepingNasaAfloat\Dialogue\Endgames\Win.dat']
    Tutorial = open_file_and_write_to_table(Tutpath[a])

    return Tutorial


def filled_rounded_rect(surface, rect, color, radius=0.4):

    """
    FilledRoundedRect(surface, rect, color, radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1

    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0, 0
    rectangle    = Surface(rect.size, SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2, SRCALPHA)
    draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle       = transform.smoothscale(circle, [int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle, (0, 0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright     = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle, pos)


def create_dialogue_box(display, text_panel_x, text_panel_y, text_panel_width, text_panel_height, color1, color2):
    panel1 = Rect(text_panel_x, text_panel_y,
                  text_panel_width, text_panel_height)
    panel2 = Rect(text_panel_x, text_panel_y,
                  text_panel_width - 10, text_panel_height - 10)

    rpanel = filled_rounded_rect(display, panel1, color2, 0.5)
    rpane2 = filled_rounded_rect(display, panel2, color1, 0.5)

    return


def create_dialogue_box2(display, text_panel_x, text_panel_y, text_panel_width, text_panel_height, color1, color2):
    panel1 = Rect(text_panel_x + 5, text_panel_y + 2,
                  text_panel_width + 1, text_panel_height + 1)
    panel2 = Rect(text_panel_x, text_panel_y,
                  text_panel_width, text_panel_height)

    rpanel = filled_rounded_rect(display, panel1, color2, 0.1)
    rpane2 = filled_rounded_rect(display, panel2, color1, 0.1)

    return


def create_top_scores_box(display, text_panel_x, text_panel_y, text_panel_width, text_panel_height, color1, color2):
    panel1 = Rect(text_panel_x + 5, text_panel_y + 2,
                  text_panel_width + 1, text_panel_height + 1)
    panel2 = Rect(text_panel_x, text_panel_y,
                  text_panel_width, text_panel_height)

    rpanel = filled_rounded_rect(display, panel1, color2, 0.1)
    rpane2 = filled_rounded_rect(display, panel2, color1, 0.1)

    return


def create_character_description_box(display, text_panel_x, text_panel_y, text_panel_width, text_panel_height, color1, color2):
    panel1 = Rect(text_panel_x + 5, text_panel_y + 2,
                  text_panel_width + 1, text_panel_height + 1)
    panel2 = Rect(text_panel_x, text_panel_y,
                  text_panel_width, text_panel_height)

    rpanel = filled_rounded_rect(display, panel1, color2, 0.5)
    rpane2 = filled_rounded_rect(display, panel2, color1, 0.5)

    return


def create_week_indicator_box(display, text_panel_x, text_panel_y, text_panel_width, text_panel_height, color1, color2):
    panel1 = Rect(text_panel_x + 5, text_panel_y + 2,
                  text_panel_width + 1, text_panel_height + 1)
    # panel2 = Rect(text_panel_x, text_panel_y,
    #               text_panel_width, text_panel_height)

    rpanel = filled_rounded_rect(display, panel1, color1, 0.5)
    # rpane2 = filled_rounded_rect(display, panel2, color1, 0.5)

    return


def random_index_list():

    random_index_list = []

    for x in range(4):
        random_index_list.append(random.randint(0, 3))

    return random_index_list


def character_position():
    a = 0
    a = random.randint(0, 3)
    position = random_index_list()[a]

    return position


def dialogue_position():
    a = 0
    a = random.randint(0, 3)
    position = random_index_list()[a]
    return position
