# https://leetcode.com/problems/construct-product-matrix/


class Solution:
    """2906. Construct Product Matrix

    Given a **0-indexed** 2D integer matrix `grid` of size `n * m`, we define a
    **0-indexed** 2D matrix `p` of size `n * m` as the **product** matrix of `grid` if
    the following condition is met:

    * Each element `p[i][j]` is calculated as the product of all elements in `grid`
    except for the element `grid[i][j]`. This product is then taken modulo `12345`.

    Return *the product matrix of* `grid`."""

    def construct_product_matrix(self, grid: list[list[int]]) -> list[list[int]]: ...

    constructProductMatrix = construct_product_matrix
