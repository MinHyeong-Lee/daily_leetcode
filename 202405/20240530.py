# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/


class Solution:
    """1442. Count Triplets That Can Form Two Arrays of Equal XOR

    Given an array of integers `arr`.

    We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k <
    arr.length)`.

    Let's define `a` and `b` as follows:

    * `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`

    * `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

    Note that **^** denotes the **bitwise-xor** operation.

    Return *the number of triplets* (`i`, `j` and `k`) Where `a == b`.

    integer로 이루어진 배열 arr이 주어진다.
    (i, j, k)라는 숫자의 조합을 얻고싶음

    규칙 a와 b는 아래와 같다.
    xor연산은 두 숫자의 값이 다르면 1, 같으면 0을 리턴한다.
    a = arr[i] xor arr[i+1] xor .... arr[j-1]
    a는 i부터 ~ j-1까지의 숫자들을 xor 연산한 것.

    b = arr[j] xor arr[j+1] xor ... arr[k]
    b는 j부터 ~ k까지의 숫자들을 xor 연산한 것.

    a == b인 (i, j, k)의 갯수를 구해라.

    """

    def count_triplets(self, arr: list[int]) -> int:
        n = len(arr)
        count = 0

        # XOR 결과물 담을 배열 선언
        xor = [0] * (n + 1)

        # 배열 전체에 대해서 XOR 연산 한바퀴 수행
        for i in range(n):
            xor[i + 1] = xor[i] ^ arr[i]

        for i in range(n):
            # i를 고정시키고
            for k in range(i + 1, n):
                # i+1값부터 k를 배열 끝까지 순회시켜서 가능한 조합 찾기
                if xor[i] == xor[k + 1]:
                    count += k - i

        return count

    countTriplets = count_triplets


temp = Solution()
arr = [2, 3, 1, 6, 7]
temp.count_triplets(arr)
