# https://leetcode.com/problems/count-number-of-trapezoids-ii/


class Solution:
    """3625. Count Number of Trapezoids II

    You are given a 2D integer array `points` where `points[i] = [xi, yi]` represents
    the coordinates of the `ith` point on the Cartesian plane.

    Return *the number of unique* *trapezoids* that can be formed by choosing any four
    distinct points from `points`.

    A**trapezoid** is a convex quadrilateral with **at least one pair** of parallel
    sides. Two lines are parallel if and only if they have the same slope."""

    def count_trapezoids(self, points: list[list[int]]) -> int: ...

    countTrapezoids = count_trapezoids
