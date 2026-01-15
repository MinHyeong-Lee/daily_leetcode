# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/


class Solution:
    """2943. Maximize Area of Square Hole in Grid

    You are given the two integers, `n` and `m` and two integer arrays, `h_bars` and
    `v_bars`. The grid has `n + 2` horizontal and `m + 2` vertical bars, creating 1 x 1
    unit cells. The bars are indexed starting from `1`.

    You can **remove** some of the bars in `h_bars` from horizontal bars and some of the
    bars in `v_bars` from vertical bars. Note that other bars are fixed and cannot be
    removed.

    Return an integer denoting the **maximum area** of a *square-shaped* hole in the
    grid, after removing some bars (possibly none)."""

    def maximize_square_hole_area(
        self, n: int, m: int, h_bars: list[int], v_bars: list[int]
    ) -> int: ...

    maximizeSquareHoleArea = maximize_square_hole_area
