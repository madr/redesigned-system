import unittest

from solutions.day_01 import Solution


class Day01TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_resolves_frequency(self):
        freq_1 = '\n'.join(['+1', '+1', '+1'])
        freq_2 = '\n'.join(['+1', '+1', '-2'])
        freq_3 = '\n'.join(['-1', '-2', '-3'])
        assert self.solution.solve(freq_1) == 3
        assert self.solution.solve(freq_2) == 0
        assert self.solution.solve(freq_3) == -6


if __name__ == '__main__':
    unittest.main()
