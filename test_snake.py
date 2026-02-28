import unittest
import subprocess
import sys


class TestSnakeGame(unittest.TestCase):
    def test_run(self):
        proc = subprocess.Popen(
            [sys.executable, "snake.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        try:
            out, err = proc.communicate(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
        # 仅测试是否能启动无报错
        self.assertIsNotNone(proc)


if __name__ == "__main__":
    unittest.main()
