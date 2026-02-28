import unittest
import snake


class TestLogic(unittest.TestCase):
    def test_snake_not_collide(self):
        # 不撞墙也不撞自己
        snake_positions = [(40, 40), (20, 40), (0, 40)]
        direction = (20, 0)
        head = (
            snake_positions[0][0] + direction[0],
            snake_positions[0][1] + direction[1],
        )
        self.assertFalse(
            head[0] < 0
            or head[0] >= snake.WINDOW_WIDTH
            or head[1] < 0
            or head[1] >= snake.WINDOW_HEIGHT
            or head in snake_positions
        )

    def test_snake_wall_collision(self):
        # 撞墙
        snake_positions = [(580, 380)]
        direction = (20, 0)
        head = (
            snake_positions[0][0] + direction[0],
            snake_positions[0][1] + direction[1],
        )
        self.assertTrue(
            head[0] < 0
            or head[0] >= snake.WINDOW_WIDTH
            or head[1] < 0
            or head[1] >= snake.WINDOW_HEIGHT
            or head in snake_positions
        )

    def test_snake_self_collision(self):
        # 撞到自己
        snake_positions = [(40, 40), (20, 40), (0, 40)]
        direction = (-20, 0)
        head = (
            snake_positions[0][0] + direction[0],
            snake_positions[0][1] + direction[1],
        )
        snake_positions.insert(0, head)
        self.assertTrue(head in snake_positions[1:])


if __name__ == "__main__":
    unittest.main()
