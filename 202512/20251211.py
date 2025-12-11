# https://leetcode.com/problems/count-covered-buildings/


class Solution:
    """3531. Count Covered Buildings

    You are given a positive integer `n`, representing an `n x n` city. You are also
    given a 2D grid `buildings`, where `buildings[i] = [x, y]` denotes a **unique**
    building located at coordinates `[x, y]`.

    A building is **covered** if there is at least one building in all **four**
    directions: left, right, above, and below.

    Return the number of **covered** buildings."""

    def count_covered_buildings(self, n: int, buildings: list[list[int]]) -> int: ...

    countCoveredBuildings = count_covered_buildings
