# https://leetcode.com/problems/cyclically-rotating-a-grid/


class Solution:
    """1914. Cyclically Rotating a Grid

    You are given an `m x n` integer matrix `grid`\u200b\u200b\u200b, where `m` and `n` are both
    **even** integers, and an integer `k`.

    The matrix is composed of several layers, which is shown in the below image, where
    each color is its own layer:

    ![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png)

    A cyclic rotation of the matrix is done by cyclically rotating **each layer** in the
    matrix. To cyclically rotate a layer once, each element in the layer will take the
    place of the adjacent element in the **counter-clockwise** direction. An example
    rotation is shown below:

    ![](https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg)

    Return *the matrix after applying* `k` *cyclic rotations to it*."""

    def rotate_grid(self, grid: list[list[int]], k: int) -> list[list[int]]: ...

    rotateGrid = rotate_grid
