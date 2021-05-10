from KeepingNasaAfloat.Sequences.Tutorial import *
from KeepingNasaAfloat.Functions.KNA_functions import *

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

Endgame = create_endgame_list(5)


class Win:

    def __init__(self, fake):

        # Set up background and self.display size

        if not fake:
            image1 = pygame.image.load('KeepingNasaAfloat\\Sprites\\Endings\\Win\\Moon_landing.jpg')
            image2 = pygame.image.load('KeepingNasaAfloat\\Sprites\\Endings\\Win\\Moon_landing2.jpg')
            self.background = [image1, image2]
            self.background[0] = pygame.transform.scale(self.background[0], (683, 683))
            self.background[1] = pygame.transform.scale(self.background[1], (1250, 683))
            pygame.mixer.music.load("KeepingNasaAfloat\\Audio\\Endings\\Win\\2001 A Space Odissey - OST.wav")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)

        else:
            image1 = pygame.image.load('KeepingNasaAfloat\\Sprites\\Endings\\Win\\Kubrick_filming_with_astronaut.jpg')
            self.background = [image1]
            self.background[0] = pygame.transform.scale(self.background[0], (1031, 683))
            pygame.mixer.music.load("KeepingNasaAfloat\\Audio\\Endings\\Win\\Chris Squire - Lucky Seven.wav")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)

        self.display = pygame.display.set_mode((455, 683))

        # Set up buttons

        self.BACK_TO_MENU_button = EndgameScreenButton(TRANSPARENT_WHITE, 55, 630, 350, 30)

        # Set up sounds

        self.s = pygame.mixer.Sound("KeepingNasaAfloat\\Audio\\Typewriter click.wav")

        # Pick over-200 or 0 outcome
        self.fake = fake

    """ 

    Text Print

    """

    def print_endgame_text(self):

        """

        Prints dialogue text during introduction to the game

        """

        font_size = 18
        text_pos = (60, 427)

        if self.fake:
            text_pos = (60, 432)
            font_size = 19

        # Set up font for introduction of the game

        font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\atwriter.ttf", font_size)

        if not self.fake:
            a = 0
        else:
            a = 1

        words = Endgame[a][1].split(' ')

        word_spacing = 10
        text_line_space = 400
        x = text_pos[0]
        y = text_pos[1]

        for word in words:
            word_surface = font.render(word, True, BLACK)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= text_line_space:
                x = text_pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            self.display.blit(word_surface, (x, y))
            x += word_width + word_spacing

    """

    Buttons

    """

    def draw_KEEP_GOING_button(self):
        self.BACK_TO_MENU_button.draw(self.display, TRANSPARENT_ANTIQUE_WHITE, ' . . . ', True)

    """

    GUIs

    """

    def redraw_endgame_gui(self, i=None, pos=None):
        self.display.fill(BLACK)
        self.display.blit(self.background[i], pos)
        Endgame_dialogue = Endgame_box(self.display, (380, 200), (455, 683))

    """

    Event reactions

    """

    def on_event_endgame(self):

        in_top_score_screen = True

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.BACK_TO_MENU_button.isOver(pos):
                    in_top_score_screen = False
                    empty_channel = pygame.mixer.find_channel()
                    empty_channel.play(self.s)
            if event.type == pygame.MOUSEMOTION:
                if self.BACK_TO_MENU_button.isOver(pos):
                    self.BACK_TO_MENU_button.color = TRANSPARENT_NASA_BLUE
                else:
                    self.BACK_TO_MENU_button.color = TRANSPARENT_WHITE
        return in_top_score_screen

    """

    Top scores

    """

    def endgame(self):

        in_top_score_screen = True
        i = 0
        pos = (0, 0)
        alpha = 255
        while in_top_score_screen:
            self.background[i].set_alpha(alpha)
            self.redraw_endgame_gui(i, pos)
            self.draw_KEEP_GOING_button()
            self.print_endgame_text()
            pygame.display.update()
            in_top_score_screen = self.on_event_endgame()
            if self.fake:
                pos = (pos[0] - 0.4, pos[1])
                if pos[0] <= - 400:
                    alpha = alpha - 1.7
                    if pos[0] <= - 500:
                        alpha = 255
                        pos = (0, 0)
            else:
                if i == 0:
                    pos = (pos[0] - 0.3, pos[1])
                    if pos[0] <= - 150:
                        alpha = alpha - 2
                        if pos[0] <= - 200:
                            alpha = 255
                            pos = (0, 0)
                            i = i + 1
                if i == 1:
                    pos = (pos[0] - 0.6, pos[1])
                    if pos[0] <= - 740:
                        alpha = alpha - 2
                        if pos[0] <= - 795:
                            alpha = 255
                            pos = (0, 0)
                            i = 0

        # pygame.mixer.music.fadeout(5000)

        for i in range(100):
            fade_surface = pygame.Surface((455, 683))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(255 * i / 1000)

            self.display.blit(fade_surface, (0, 0))

            pygame.display.update()
            pygame.time.delay(25)


# end = Win(False)
# end.endgame()