import pygame
import random
import sys

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 192, 70)
RED = (255, 80, 80)
BLACK = (33, 36, 41)
GRAY = (120, 120, 120)
BG_TOP = (44, 51, 90)
BG_BOTTOM = (19, 17, 43)


def draw_gradient(screen, color_top, color_bottom):
    # 渐变背景
    rect = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    for y in range(WINDOW_HEIGHT):
        ratio = y / WINDOW_HEIGHT
        r = int(color_top[0] * (1-ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1-ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1-ratio) + color_bottom[2] * ratio)
        pygame.draw.line(rect, (r,g,b), (0, y), (WINDOW_WIDTH, y))
    screen.blit(rect, (0, 0))


def draw_snake(screen, snake):
    # 蛇头高亮（圆+边框），身体渐变
    for i, pos in enumerate(snake):
        center = (pos[0]+CELL_SIZE//2, pos[1]+CELL_SIZE//2)
        if i == 0:
            pygame.draw.circle(screen, WHITE, center, CELL_SIZE//2+2)
            pygame.draw.circle(screen, GREEN, center, CELL_SIZE//2)
        else:
            c = int(70+(180-70)*i/len(snake))
            color = (c, 220-c//2, 80+c//5)
            pygame.draw.circle(screen, color, center, CELL_SIZE//2-1)


def draw_food(screen, position):
    center = (position[0]+CELL_SIZE//2, position[1]+CELL_SIZE//2)
    pygame.draw.circle(screen, RED, center, CELL_SIZE//2-2)
    pygame.draw.circle(screen, WHITE, center, 4)


def draw_score(screen, font, score):
    text = font.render(f"分数: {score}", True, WHITE)
    shadow = font.render(f"分数: {score}", True, BLACK)
    screen.blit(shadow, (7, 7))
    screen.blit(text, (5, 5))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("贪吃蛇Plus")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("SimHei", 32, bold=True)

    snake = [(CELL_SIZE * 6, CELL_SIZE * 7)]
    direction = (CELL_SIZE, 0)
    food = (random.randrange(0, WINDOW_WIDTH, CELL_SIZE), random.randrange(0, WINDOW_HEIGHT, CELL_SIZE))
    score = 0
    running = True
    while running:
        clock.tick(13)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if (
            new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH
            or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT
            or new_head in snake
        ):
            running = False
        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            while True:
                food = (random.randrange(0, WINDOW_WIDTH, CELL_SIZE), random.randrange(0, WINDOW_HEIGHT, CELL_SIZE))
                if food not in snake:
                    break
        else:
            snake.pop()
        draw_gradient(screen, BG_TOP, BG_BOTTOM)
        draw_food(screen, food)
        draw_snake(screen, snake)
        draw_score(screen, font, score)
        pygame.display.flip()

    pygame.quit()
    print(f"游戏结束，分数: {score}")

if __name__ == '__main__':
    main()
