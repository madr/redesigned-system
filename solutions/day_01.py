from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '01.txt'

    def __str__(self):
        return 'Day 01: Chronal Calibration'

    def solve(self, puzzle_input, freq=0):
        freq_changes = map(int, puzzle_input.splitlines())
        for n in freq_changes:
            freq += n
        return freq

    def solve_again(self, puzzle_input):
        pass


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
