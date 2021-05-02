import pygame
import pygame.gfxdraw


class View:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 128, 0)

    def __init__(self, width, height, rows):
        self._width = width
        self._height = height
        self._rows = rows
        self._delta = self._width / self._rows

        self._screen = pygame.display.set_mode((width, height))
        self._screen.fill(self.BLACK)

    def draw_grid(self, color):

        for i in range(self._rows + 1):
            pygame.draw.line(self._screen, color, (0, i * self._delta), (self._width, i * self._delta))

        for j in range(self._rows):
            pygame.draw.line(self._screen, color, (j * self._delta, 0), (j * self._delta, self._width))

    def fill(self, color):
        self._screen.fill(color)

    def mouse_position_to_index(self, pos):
        try:
            x = int(pos[0] / self._delta)
            y = int(pos[1] / self._delta)

            return x, y
        except IndexError:
            pass

    def fill_grid(self, grid):
        for i in range(self._rows):
            for j in range(self._rows):
                if grid[i][j] == 1:
                    pygame.gfxdraw.box(self._screen,
                                       pygame.Rect(i * self._delta, j * self._delta, self._delta, self._delta), self.WHITE)

    def set_rows(self, rows):
        self._rows = rows
        self._delta = self._width / self._rows

    def get_screen(self):
        return self._screen