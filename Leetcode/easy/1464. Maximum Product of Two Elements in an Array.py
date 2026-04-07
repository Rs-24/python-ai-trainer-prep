# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        first = 0
        second = 0
        for num in nums:
            if num >= first: 
                second = first
                first = num
            elif num > second:
                second = num
        return (first - 1) * (second - 1)


