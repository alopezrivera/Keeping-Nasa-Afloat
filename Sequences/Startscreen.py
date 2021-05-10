import pygame

from KeepingNasaAfloat.Classes.Button import *


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
DARK_YELLOW = (220, 190, 56)
BACKGROUND_BROWN = (252, 244, 218)
SOVIET_RED = (179, 0, 0)
TURQUESA = (0, 255, 222)
DOLLAR_GREEN = (0, 128, 4)
UNREMARKABLE_GREY = (164, 164, 164)

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
pygame.init()


class Startscreen:

    def __init__(self, display, size):

        """

        Copies screen at the end of the initial fade-in

        """

        self.display = display
        self.size = size

        self.play_button = StartButton(WHITE, 37.5, 385, 380, 70)
        self.play_easy_button = StartButton(WHITE, 37.5, 475, 380, 70)
        self.top_scores_button = StartButton(WHITE, 37.5, 565, 380, 70)

        # Background image
        self.background = pygame.image.load(
            'KeepingNasaAfloat\\Sprites\\startscreen_take_off.jpg')
        self.background = pygame.transform.scale(self.background, self.size)

        # Sound set-up
        self.s = pygame.mixer.Sound(
            "KeepingNasaAfloat\\Audio\\Typewriter click.wav")
        self.fadenoise = pygame.mixer.Sound(
            "KeepingNasaAfloat\\Audio\\Liftoff.wav")
        self.fadenoise2 = pygame.mixer.Sound(
            "KeepingNasaAfloat\\Audio\\Rocket Launch.wav")

        # Title setup
        Title_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Southern Aire\\SouthernAire_Personal_Use_Only.ttf", 100)
        NASA_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\NASA.otf", 110)
        Credits_font = pygame.font.Font("KeepingNasaAfloat\\Fonts\\Copyrighted\\Brannboll\\BrannbollFS_PERSONAL.ttf", 20)

        fonts = [Title_font, NASA_font, Title_font, Credits_font]
        title = ['Keeping', 'NASA', 'Afloat!', "Antonio Lopez Rivera and Roman Chivas's"]
        colors = [WHITE, NASA_BLUE, WHITE, WHITE]
        shadow_colors = [ANTIQUE_WHITE, NASA_YELLOW, ANTIQUE_WHITE, ANTIQUE_WHITE]

        pos = (40, 60)
        shadow_pos = (pos[0] + 3, pos[1] + 3)

        for i in range(4):
            if i == 1:
                a = -17
                b = 80
                pos = (pos[0] + a, pos[1] + b)
                shadow_pos = (shadow_pos[0] + a + 2, shadow_pos[1] + b)
            if i == 2:
                a = 130
                b = 72
                pos = (pos[0] + a, pos[1] + b)
                shadow_pos = (shadow_pos[0] + a - 2, shadow_pos[1] + b)
            if i == 3:
                pos = (30, 50)
                shadow_pos = (31, 51)

            word = fonts[i].render(title[i], True, colors[i])
            word_shadow = fonts[i].render(title[i], True, shadow_colors[i])
            self.background.blit(word_shadow, shadow_pos)
            self.background.blit(word, pos)

            self.display.blit(self.background, (0, 0))
            self.play_button.draw(self.display, ANTIQUE_WHITE, 'Start')
            self.play_easy_button.draw(self.display, ANTIQUE_WHITE, 'Easy Mode')
            self.top_scores_button.draw(self.display, ANTIQUE_WHITE, 'Top scores')

    def on_event(self, music=True):

        """

        Makes buttons available to choose gameplay mode or top scores screen

        """

        if music is True:
            pygame.mixer.music.load('KeepingNasaAfloat\\Audio\\Louis Armstrong - La Vie en Rose - Shortened.wav')
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(1)

        choice = False

        while not choice:

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.MOUSEMOTION:
                    if self.play_button.isOver(pos):
                        self.play_button.color = GREEN
                    else:
                        self.play_button.color = WHITE
                    if self.play_easy_button.isOver(pos):
                        self.play_easy_button.color = GREEN
                    else:
                        self.play_easy_button.color = WHITE
                    if self.top_scores_button.isOver(pos):
                        self.top_scores_button.color = GREEN
                    else:
                        self.top_scores_button.color = WHITE

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.play_button.isOver(pos):
                        choice = True
                        empty_channel = pygame.mixer.find_channel()
                        empty_channel.play(self.s)
                        path = 1
                    if self.play_easy_button.isOver(pos):
                        choice = True
                        empty_channel = pygame.mixer.find_channel()
                        empty_channel.play(self.s)
                        path = 2
                    if self.top_scores_button.isOver(pos):
                        choice = True
                        empty_channel = pygame.mixer.find_channel()
                        empty_channel.play(self.s)
                        path = 3

            self.display.blit(self.background, (0, 0))
            self.play_button.draw(self.display, ANTIQUE_WHITE, 'Start')
            self.play_easy_button.draw(self.display, ANTIQUE_WHITE, 'Easy Mode')
            self.top_scores_button.draw(self.display, ANTIQUE_WHITE, 'Top Scores')
            pygame.display.update()

        return path

    def roll_change(self):
        pygame.time.delay(100)
        empty_channel = pygame.mixer.find_channel()
        empty_channel.play(self.fadenoise)
        empty_channel_2 = pygame.mixer.find_channel()
        empty_channel_2.play(self.fadenoise2)
        pygame.mixer.music.fadeout(3000)

        for i in range(80):
            fade_surface = pygame.Surface((455, 683))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(255 * i / 1000)

            self.display.blit(fade_surface, (0, 0))

            pygame.display.update()
            pygame.time.delay(25)
