# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/

from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        count = 0
        total = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                count += 1
        return total // count if count > 0 else 0


