import copy


class Grid:
    def __init__(self, rows):
        self._rows = rows
        self._grid_array = [[0 for x in range(self._rows)] for y in range(self._rows)]

    def cell_birth(self, pos):
        try:
            self._grid_array[pos[0]][pos[1]] = 1
        except IndexError:
            pass

    def cell_kill(self, pos):
        try:
            self._grid_array[pos[0]][pos[1]] = 0
        except IndexError:
            pass

    def neighbors(self, i, j):
        n = 0
        if i + 1 < len(self._grid_array) and j - 1 >= 0 and self._grid_array[i + 1][j - 1]:
            n += 1

        if i - 1 >= 0 and j - 1 >= 0 and self._grid_array[i - 1][j - 1]:
            n += 1

        if j - 1 >= 0 and self._grid_array[i][j - 1]:
            n += 1

        if i + 1 < len(self._grid_array) and self._grid_array[i + 1][j]:
            n += 1

        if i + 1 < len(self._grid_array) and j + 1 < len(self._grid_array[0]) and self._grid_array[i + 1][j + 1]:
            n += 1

        if i - 1 >= 0 and j + 1 < len(self._grid_array[0]) and self._grid_array[i - 1][j + 1]:
            n += 1

        if j + 1 < len(self._grid_array[0]) and self._grid_array[i][j + 1]:
            n += 1

        if i - 1 >= 0 and self._grid_array[i - 1][j]:
            n += 1

        return n

    def next_step(self):
        next = copy.deepcopy(self._grid_array)
        for i in range(len(self._grid_array)):
            for j in range(len(self._grid_array[i])):
                num_neighbors = self.neighbors(i, j)

                if self._grid_array[i][j] == 1 and num_neighbors != 2 and num_neighbors != 3:
                    next[i][j] = 0

                if num_neighbors == 3 and self._grid_array[i][j] != 1:
                    next[i][j] = 1

        self._grid_array = next

    def get_grid(self):
        return self._grid_array

    def clear_grid(self):
        self._grid_array = [[0 for x in range(self._rows)] for y in range(self._rows)]

    def set_rows(self, rows):
        self._rows = rows
        self.clear_grid()