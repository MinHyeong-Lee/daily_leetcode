# https://leetcode.com/problems/single-number-iii/


class Solution:
    """260. Single Number III

    Given an integer array `nums`, in which exactly two elements appear only once and
    all the other elements appear exactly twice. Find the two elements that appear only
    once. You can return the answer in **any order**.

    You must write an algorithm that runs in linear runtime complexity and uses only
    constant extra space.

    정수 배열 nums가 있다.
    두 종류의 elements는 오직 1개씩만 들어있고
    나머지 모든 elements는 2개씩 들어있다.
    1개씩만 들어있는 숫자를 찾아라. 리턴할때 sorting은 상관없음.
    
    중복값 찾을때 hash map(dict)를 사용하는게 좋음
    """

    def single_number(self, nums: list[int]) -> list[int]:
        frequency = {}
        
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
                
        unique_numbers = [num for num in frequency if frequency[num] == 1]
        
        print(unique_numbers)
        return unique_numbers

    singleNumber = single_number

temp = Solution()
temp.singleNumber([1, 2, 1, 3, 2, 5])
temp.singleNumber([-1, 0])