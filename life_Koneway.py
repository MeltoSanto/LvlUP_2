import pygame
import random

# размер поля
n = 50

# инициализация Pygame
pygame.init()

# создание окна
window = pygame.display.set_mode((n*10, n*10))
pygame.display.set_caption("Игра Жизнь от команды - Альфа")

# создание поля
grid = [[random.choice([0, 1]) for j in range(n)] for i in range(n)]

# функция для отрисовки поля
def draw_grid():
    for i in range(n):
        for j in range(n):
            color = (130, 255, 200) if grid[i][j] else (0, 0, 0)
            pygame.draw.rect(window, color, (j*10, i*10, 10, 10))

# функция для обновления состояния поля
def update_grid():
    new_grid = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            count = sum([grid[x][y] for x in range(max(0, i-1), min(n, i+2)) for y in range(max(0, j-1), min(n, j+2))]) - grid[i][j]
            if grid[i][j] and (count == 2 or count == 3):
                new_grid[i][j] = 1
            elif not grid[i][j] and count == 3:
                new_grid[i][j] = 1
    return new_grid

# основной цикл игры
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # отрисовка поля и обновление состояния
    draw_grid()
    grid = update_grid()

    # обновление экрана
    pygame.display.update()

# завершение Pygame
pygame.quit()