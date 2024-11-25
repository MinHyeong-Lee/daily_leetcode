# https://leetcode.com/problems/sliding-puzzle/


class Solution:
    """773. Sliding Puzzle

    On an `2 x 3` board, there are five tiles labeled from `1` to `5`, and an empty
    square represented by `0`. A **move** consists of choosing `0` and a 4-directionally
    adjacent number and swapping it.

    The state of the board is solved if and only if the board is `[[1,2,3],[4,5,0]]`.

    Given the puzzle board `board`, return *the least number of moves required so that
    the state of the board is solved*. If it is impossible for the state of the board to
    be solved, return `-1`."""

    def sliding_puzzle(self, board: list[list[int]]) -> int: ...

    slidingPuzzle = sliding_puzzle
