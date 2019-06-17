from GAME_pygame.KeepingNasaAfloat.Classes.Button import *

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
pygame.init()


class Intro_screen:

    def __init__(self, display, size):
        self.display = display
        self.size = size

        self.play_button = StartButton(WHITE, 37.5, 385, 380, 70)
        self.play_easy_button = StartButton(WHITE, 37.5, 475, 380, 70)
        self.top_scores_button = StartButton(WHITE, 37.5, 565, 380, 70)

    def let_the_game_begin(self):

        """

        Countdown sound, title screen fade in

        """

        # Countdown sound effect
        s = pygame.mixer.Sound('C:\\Users\\xXY4n\\OneDrive\\Escritorio\\Python\\GAME_pygame\\KeepingNasaAfloat\\'
                               'Audio\\Countdown.wav')
        empty_channel = pygame.mixer.find_channel()
        empty_channel.play(s)
        pygame.mixer.music.load('C:\\Users\\xXY4n\\OneDrive\\Escritorio\\Python\\GAME_pygame\\KeepingNasaAfloat\\'
                                'Audio\\Louis Armstrong - La Vie en Rose.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        # Background image
        background = pygame.image.load(
            'C:\\Users\\xXY4n\\OneDrive\\Escritorio\\Python\\GAME_pygame\\KeepingNasaAfloat\\Sprites\\'
            'startscreen_take_off.jpg')
        background = pygame.transform.scale(background, self.size)

        # Title setup
        Title_font = pygame.font.Font("C:\\Users\\xXY4n\\OneDrive\\Escritorio\\Python\\GAME_pygame\\"
                                      "KeepingNasaAfloat\\Fonts\\Copyrighted\\Southern Aire\\"
                                      "SouthernAire_Personal_Use_Only.ttf", 100)

        NASA_font = pygame.font.Font("C:\\Users\\xXY4n\\OneDrive\\Escritorio\\Python\\GAME_pygame\\"
                                     "KeepingNasaAfloat\\Fonts\\NASA.otf", 110)

        Credits_font = pygame.font.Font("C:\\Users\\xXY4n\\OneDrive\\Escritorio\\Python\\GAME_pygame\\"
                                        "KeepingNasaAfloat\\Fonts\\Copyrighted\\Brannboll\\"
                                        "BrannbollFS_PERSONAL.ttf", 20)

        fonts = [Title_font, NASA_font, Title_font, Credits_font]
        title = ['Keeping', 'NASA', 'Afloat!', "Antonio Lopez Rivera and Roman Chiva's"]
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
            background.blit(word_shadow, shadow_pos)
            background.blit(word, pos)

        pygame.time.delay(80)

        start_cutscene = True
        start_time = pygame.time.get_ticks()

        curtain = pygame.Surface((455, 683))
        curtain.fill(BLACK)

        """
        
        Alternative fade-in start animation was discarded in favor of Grav_Sim
        
        """

        while start_cutscene:

            dt = pygame.time.get_ticks() - start_time

            alpha = 255 - dt/20

            curtain.set_alpha(alpha)

            self.display.blit(background, (0, 0))
            self.display.blit(curtain, (0, 0))

            if pygame.time.get_ticks() - start_time >= 5800:
                self.play_button.draw(self.display, ANTIQUE_WHITE, 'Start')
                if pygame.time.get_ticks() - start_time >= 7800:
                    self.play_easy_button.draw(self.display, ANTIQUE_WHITE, 'Easy Mode')
                    if pygame.time.get_ticks() - start_time >= 9800:
                        self.top_scores_button.draw(self.display, ANTIQUE_WHITE, 'Top Scores')
                        start_cutscene = False

            pygame.display.update()

