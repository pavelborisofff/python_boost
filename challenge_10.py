# BFS algorithm
import time
import turtle
from typing import List


def draw(drawer: turtle.Turtle, turn_num: int, matrix: List[List], array: List[List]):
    cell = 25
    font_size = 25
    width = len(matrix[0])
    height = len(matrix)

    drawer.penup()
    drawer.color('black')
    drawer.goto(0, cell * height / 2 + font_size)
    drawer.pendown()
    drawer.write(f'### {turn_num} ###', align='center', font=('Serif', font_size))
    drawer.penup()

    drawer.pendown()
    drawer.goto(-cell * width / 2 + cell / 2, cell * height / 2)

    for y in range(height):
        for x in range(width):

            if array[y][x] == 1:
                drawer.color('black')
            else:
                if matrix[y][x] == 0:
                    drawer.color('gray')
                elif matrix[y][x] == turn_num:
                    drawer.color('yellow')
                elif matrix[y][x] == turn_num + 1:
                    drawer.color('red')
                else:
                    drawer.color('green')

            drawer.dot(10)
            drawer.penup()
            cx, cy = drawer.pos()
            drawer.goto(cx + cell, cy)

        cx, cy = drawer.pos()
        drawer.goto(cx - width * cell, cy - cell)


def turn(turn_num: int, matrix: List[List], array: List[List]):
    height = len(matrix)
    width = len(matrix[0])
    passable = False  # Case of dead end

    for y in range(height):
        for x in range(width):
            if matrix[y][x] == turn_num:
                up, left, down, right = (y - 1, x - 1, y + 1, x + 1)
                # Wave to upper cell
                if up >= 0 and matrix[up][x] == 0 and array[up][x] == 0:
                    matrix[up][x] = turn_num + 1
                    passable = True
                # Wave to left cell
                if left >= 0 and matrix[y][left] == 0 and array[y][left] == 0:
                    matrix[y][left] = turn_num + 1
                    passable = True
                # Wave to down cell
                if down < height and matrix[down][x] == 0 and array[down][x] == 0:
                    matrix[down][x] = turn_num + 1
                    passable = True
                # Wave to right cell
                if right < width and matrix[y][right] == 0 and array[y][right] == 0:
                    matrix[y][right] = turn_num + 1
                    passable = True

    return passable


def can_exit(array: List[List]) -> bool:
    matrix = [[0 for _ in range(len(array[0]))] for _ in range(len(array))]

    sy, sx = (0, 0)
    ey, ex = (len(matrix) - 1, len(matrix[0]) - 1)

    matrix[sy][sx] = 1
    wave_num = 0

    t = turtle.Turtle()

    while matrix[ey][ex] == 0:

        turtle.clearscreen()
        turtle.tracer(0, 0)

        wave_num += 1
        result = turn(wave_num, matrix, array)

        draw(t, wave_num, matrix, array)
        turtle.update()
        time.sleep(1)

        if not result:
            break

    turtle.done()

    return matrix[ey][ex] > 0


assert can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]) == True

# assert can_exit([
#   [0, 1, 1, 1, 1, 1, 1],
#   [0, 0, 1, 0, 0, 1, 1],
#   [1, 0, 0, 0, 0, 1, 1],
#   [1, 1, 0, 1, 0, 0, 1],
#   [1, 1, 0, 0, 1, 1, 1]
# ]) == False
# В этом лабиринте одни тупики!

# assert can_exit([
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 1, 1, 1, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 1]
# ]) == False
# Выход так близко, но недостижим!

# assert can_exit([
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 0]
# ]) == True
#
# assert can_exit([
#   [0, 1, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 1, 1, 0],
#   [0, 1, 0, 1, 0, 0, 0],
#   [0, 1, 0, 1, 0, 1, 1],
#   [0, 0, 0, 1, 0, 0, 0]
# ]) == True
