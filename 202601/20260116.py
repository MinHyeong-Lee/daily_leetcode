# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/


class Solution:
    """2975. Maximum Square Area by Removing Fences From a Field

    There is a large `(m - 1) x (n - 1)` rectangular field with corners at `(1, 1)` and
    `(m, n)` containing some horizontal and vertical fences given in arrays `h_fences`
    and `v_fences` respectively.

    Horizontal fences are from the coordinates `(h_fences[i], 1)` to `(h_fences[i], n)`
    and vertical fences are from the coordinates `(1, v_fences[i])` to `(m,
    v_fences[i])`.

    Return *the **maximum** area of a **square** field that can be formed by
    **removing** some fences (**possibly none**) or* `-1` *if it is impossible to make a
    square field*.

    Since the answer may be large, return it **modulo** `109 + 7`.

    **Note:** The field is surrounded by two horizontal fences from the coordinates `(1,
    1)` to `(1, n)` and `(m, 1)` to `(m, n)` and two vertical fences from the
    coordinates `(1, 1)` to `(m, 1)` and `(1, n)` to `(m, n)`. These fences **cannot**
    be removed."""

    def maximize_square_area(
        self, m: int, n: int, h_fences: list[int], v_fences: list[int]
    ) -> int: ...

    maximizeSquareArea = maximize_square_area
