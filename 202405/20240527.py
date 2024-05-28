# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/


class Solution:
    """1608. Special Array With X Elements Greater Than or Equal X

    You are given an array `nums` of non-negative integers. `nums` is considered
    **special** if there exists a number `x` such that there are **exactly** `x` numbers
    in `nums` that are **greater than or equal to** `x`.

    Notice that `x` **does not** have to be an element in `nums`.

    Return `x` *if the array is **special**, otherwise, return* `-1`. It can be proven
    that if `nums` is special, the value for `x` is **unique**.

    """

    def special_array(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n^2)
        """
        # special = 0
        # while True:
        #     count = 0
        #     for num in nums:
        #         if num >= special:
        #             count += 1
        #         if count > special:
        #             break

        #     if count == special:
        #         return special

        #     special += 1
        #     if special > 100:
        #         return -1

        """
        Better solution pythonic
        """

        nums.sort()
        n = len(nums)
        for x in range(n + 1):
            count = sum(1 for num in nums if num >= x)

            if count == x:
                return x

        return -1

    specialArray = special_array


sol = Solution()
a = sol.specialArray([0, 4, 3, 4, 0])
print(a)
