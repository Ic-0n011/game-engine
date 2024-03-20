#import keyboard
from os import system
system('cls')
EMPTY = '█'



class Cell():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.img = EMPTY

    def __str__(self) -> str:
        return f"{self.img}"


class Screen():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = dict()
        self.make_cells()

    def make_cells(self):
        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                self.cells[(x, y)] = Cell(x, y)

    def get_cell(self, x, y) -> Cell:
        return self.cells[(x, y)]

    def draw(self):
        screen = ''
        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                screen += int(self.get_cell(x, y))
            screen += '\n'
        print(screen)

    def on_press(self):
        pass


screen = Screen(5, 10)
#keyboard.on_press(screen.on_press)

while True:
    print('\033[0;0H', end='')
    screen.draw()
