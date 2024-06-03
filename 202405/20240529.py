# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/


class Solution:
    """1404. Number of Steps to Reduce a Number in Binary Representation to One

    Given the binary representation of an integer as a string `s`, return *the number of
    steps to reduce it to* `1` *under the following rules*:

    * If the current number is even, you have to divide it by `2`.

    * If the current number is odd, you have to add `1` to it.

    It is guaranteed that you can always reach one for all test cases.

    2진수로 표현된 정수가 string type 's'로 주어진다.
    아래의 규칙에 의거하여 1로 가기위해 몇 단계가 필요한지 찾아라.

    1) 현재 숫자가 짝수면 2로 나눠라
    2) 현재 숫자가 홀수면 1을 더해라.

    테스트 케이스의 모든 케이스에 대해 경우의 수는 한가지임을 보장한다.

    우선 1101이란 숫자가 주어지면 십진수로 변형해야 함.
    """

    def num_steps(self, s: str) -> int:
        decimal_number = int(s, 2)
        step = 0
        while True:
            if decimal_number == 1:
                break
            if decimal_number % 2 == 0:
                decimal_number //= 2
            elif decimal_number % 2 == 1:
                decimal_number += 1
            step += 1

        return step

    numSteps = num_steps
