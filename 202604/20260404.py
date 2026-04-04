# https://leetcode.com/problems/decode-the-slanted-ciphertext/


class Solution:
    """2075. Decode the Slanted Ciphertext

    A string `originalText` is encoded using a **slanted transposition cipher** to a
    string `encoded_text` with the help of a matrix having a **fixed number of rows**
    `rows`.

    `originalText` is placed first in a top-left to bottom-right manner.

    ![](https://assets.leetcode.com/uploads/2021/11/07/exa11.png)

    The blue cells are filled first, followed by the red cells, then the yellow cells,
    and so on, until we reach the end of `originalText`. The arrow indicates the order
    in which the cells are filled. All empty cells are filled with `' '`. The number of
    columns is chosen such that the rightmost column will **not be empty** after filling
    in `originalText`.

    `encoded_text` is then formed by appending all characters of the matrix in a row-
    wise fashion.

    ![](https://assets.leetcode.com/uploads/2021/11/07/exa12.png)

    The characters in the blue cells are appended first to `encoded_text`, then the red
    cells, and so on, and finally the yellow cells. The arrow indicates the order in
    which the cells are accessed.

    For example, if `originalText = "cipher"` and `rows = 3`, then we encode it in the
    following manner:

    ![](https://assets.leetcode.com/uploads/2021/10/25/desc2.png)

    The blue arrows depict how `originalText` is placed in the matrix, and the red
    arrows denote the order in which `encoded_text` is formed. In the above example,
    `encoded_text = "ch ie pr"`.

    Given the encoded string `encoded_text` and number of rows `rows`, return *the
    original string* `originalText`.

    **Note:** `originalText` **does not** have any trailing spaces `' '`. The test cases
    are generated such that there is only one possible `originalText`."""

    def decode_ciphertext(self, encoded_text: str, rows: int) -> str: ...

    decodeCiphertext = decode_ciphertext
