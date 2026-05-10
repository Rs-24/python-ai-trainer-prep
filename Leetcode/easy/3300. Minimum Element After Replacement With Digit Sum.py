# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/

from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        # Time: O(n log x), n = len(nums), x = average number in nums
        # Space: O(1)
        def get_sum(x: int) -> int:
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total
        best = float("inf")
        for num in nums:
            best = min(best, get_sum(num))
        return best


