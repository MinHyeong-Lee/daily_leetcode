# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/


class Solution:
    """3047. Find the Largest Area of Square Inside Two Rectangles

    There exist `n` rectangles in a 2D plane with edges parallel to the x and y axis.
    You are given two 2D integer arrays `bottom_left` and `top_right` where
    `bottom_left[i] = [a_i, b_i]` and `top_right[i] = [c_i, d_i]` represent the
    **bottom-left** and **top-right** coordinates of the `ith` rectangle, respectively.

    You need to find the **maximum** area of a **square** that can fit inside the
    intersecting region of at least two rectangles. Return `0` if such a square does not
    exist."""

    def largest_square_area(
        self, bottom_left: list[list[int]], top_right: list[list[int]]
    ) -> int: ...

    largestSquareArea = largest_square_area
