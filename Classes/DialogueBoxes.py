from KeepingNasaAfloat.Classes.Button import *

# Colors

BLACK = (0, 0, 0)
TRANSPARENT_WHITE = (255, 255, 255, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TRANSPARENT_ANTIQUE_WHITE = (139, 131, 120, 0)


class IntroDialogueBox:

    def __init__(self, screen, dim, display_dim):
        """

        This class allows for the creation of a rectangular (filleted) box upon which to write any text needed at
        some point in the game. These dialogue boxes make up the "skeleton" of the game's GUI.
        The following classes are based on this one and are fine tuned to fit the needs of the game at various points.
        Names are hopefully self-explanatory enough as to be understood without the need for more docstrings.

        """
        pygame.init()

        basedim = 200

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 470 + (basedim - dim[1])

        create_dialogue_box2(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                             WHITE, ANTIQUE_WHITE)

    def show(self, screen):
        """

        Refreshes screen.

        """
        pygame.display.flip()


class MainDialogueBox:

    def __init__(self, screen, dim, display_dim):

        pygame.init()

        basedim = 200

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 465 + (basedim - dim[1])

        create_dialogue_box2(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                             WHITE, ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()


class Intro_description_box:

    def __init__(self, screen, dim, display_dim):

        pygame.init()

        basedim = 195

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 240 + (basedim - dim[1])

        create_character_description_box(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                                         WHITE, ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()


class Top_scores_description_box:

    def __init__(self, screen, dim, display_dim):

        pygame.init()

        basedim = 300

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 240 + (basedim - dim[1])

        create_top_scores_box(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                              TRANSPARENT_WHITE, TRANSPARENT_ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()


class Endgame_box:

    def __init__(self, screen, dim, display_dim):

        pygame.init()

        basedim = 380

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 240 + (basedim - dim[1])

        create_top_scores_box(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                              TRANSPARENT_WHITE, TRANSPARENT_ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()


class Character_description_box:

    def __init__(self, screen, dim, display_dim):

        pygame.init()

        basedim = 200

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 240 + (basedim - dim[1])

        create_character_description_box(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                                         WHITE, ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()


class Point_indicator_box:

    def __init__(self, screen, dim, display_dim):

        pygame.init()

        basedim = 200

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = (display_dim[0]-dim[0])/2 + 1
        self.text_panel_y = 15

        create_character_description_box(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                                         WHITE, ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()


class Week_indicator:

    def __init__(self, screen, dim, display_dim, i):

        pygame.init()

        basedim = 105

        self.text_panel_width = dim[0]
        self.text_panel_height = dim[1]
        self.text_panel_x = 328
        self.text_panel_y = basedim

        create_week_indicator_box(screen, self.text_panel_x, self.text_panel_y, self.text_panel_width, self.text_panel_height,
                                         WHITE, ANTIQUE_WHITE)

    def show(self, screen):
        pygame.display.flip()
