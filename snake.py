import pygame
import random
import sys

# 游戏窗口参数
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20

# 颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def draw_block(screen, color, position):
    block = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, block)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("贪吃蛇")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("SimHei", 24)

    snake = [(CELL_SIZE * 5, CELL_SIZE * 5)]
    direction = (CELL_SIZE, 0)
    food = (
        random.randrange(0, WINDOW_WIDTH, CELL_SIZE),
        random.randrange(0, WINDOW_HEIGHT, CELL_SIZE),
    )

    score = 0
    running = True
    while running:
        clock.tick(10)
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

        # 判定失败
        if (
            new_head[0] < 0
            or new_head[0] >= WINDOW_WIDTH
            or new_head[1] < 0
            or new_head[1] >= WINDOW_HEIGHT
            or new_head in snake
        ):
            running = False

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = (
                random.randrange(0, WINDOW_WIDTH, CELL_SIZE),
                random.randrange(0, WINDOW_HEIGHT, CELL_SIZE),
            )
        else:
            snake.pop()

        screen.fill(BLACK)
        for pos in snake:
            draw_block(screen, GREEN, pos)
        draw_block(screen, RED, food)
        text = font.render(f"分数: {score}", True, WHITE)
        screen.blit(text, (5, 5))
        pygame.display.flip()

    pygame.quit()
    print(f"游戏结束，分数: {score}")


if __name__ == "__main__":
    main()
