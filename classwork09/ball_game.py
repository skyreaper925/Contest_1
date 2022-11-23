import pygame
import random
from pygame.draw import *
from random import randint

pygame.init()

LENGTH = 1200
HEIGHT = 700
print(" Напишите Ваше имя (без пробела): ")
nickname = input()

FPS = 60  # Частота кадров
screen = pygame.display.set_mode((LENGTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():

    '''
    Создание произвольного круга.
    x, y - координата центра круга
    vx, vy - скорость движения круга
    r - радиус круга
    color - цвет закраски круга
    coordinates - массив значений координат, скоростей и цветов кругов
    '''

    coordinates = []
    for i in range(randint(1, 10)):
        r = randint(30, 50)
        x = randint(2*r, LENGTH - 2*r)
        y = randint(2*r, HEIGHT - 2*r)
        vx = randint(-100, 100)
        vy = randint(-100, 100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        coordinates.append([x, y, vx, vy, r, color])
    return coordinates


def click(event, coordinates, score):

    '''
    Проверка на попадание указателя мыши в область круга и написание Click! в командной строке
    coordinates - двумерный массив координат кругов
    score - количество очков до щелчка мыши
    '''

    for i in range(len(coordinates)):
        if (event.pos[0] - coordinates[i][0]) ** 2 + (event.pos[1] - coordinates[i][1]) ** 2 <= coordinates[i][-2] ** 2:
            score += 1
            print('Click!', score)
    return score


def moving(coordinates):

    '''
    Движение кругов и отражение от границ окна
    X, Y - размеры окна
    '''

    for i in range(len(coordinates)):
        if (coordinates[i][0] <= coordinates[i][-2]):
            coordinates[i][2] = random.randrange(0, 100, 1)
        elif (LENGTH - coordinates[i][0] <= coordinates[i][-2]):
            coordinates[i][2] = random.randrange(-100, 0, 1)
        elif (coordinates[i][1] <= coordinates[i][-2]):
            coordinates[i][3] = random.randrange(0, 100, 1)
        elif (HEIGHT - coordinates[i][1] <= coordinates[i][-2]):
            coordinates[i][3] = random.randrange(-100, 0, 1)
        coordinates[i][0] = coordinates[i][0] + coordinates[i][2] / 10
        coordinates[i][1] = coordinates[i][1] + coordinates[i][3] / 10
        circle(screen, coordinates[i][-1], (int(coordinates[i][0]), int(coordinates[i][1])), coordinates[i][-2])
    return coordinates


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0

Start = False

coordinates = new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif Start and event.type == pygame.MOUSEBUTTONDOWN:
            score = click(event, coordinates, score)  # Считывание нажатия и проверка на область
    Start = True
    coordinates = moving(coordinates)  # Считывание массива координат
    pygame.display.update()
    screen.fill(BLACK)
    if score >= 3:
        finished = True


with open("rating.txt", "r") as f:       #Считывание старой таблицы
    a = list(map(lambda x: [y for y in x.rstrip().split()], f.readlines()))
Find = False
for s in a:       #Поиск имени и изменение результата
    s[1] = int(s[1])
    if s[0] == nickname:
        Find = True
    if s[0] == nickname and s[1] < score:
        s[1] = score
if not Find:
    a.append([nickname, score])
a = sorted(a, key = lambda x: (-x[1], x[0]))
for s in a:
    s[1] = str(s[1])
with open("rating.txt", "w") as f:         #Запись новой таблицы
    f.writelines([" ".join(x) + "\n" for x in a])

pygame.quit()