# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-arithmetic-triplets/description/

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set(nums)
        count = 0
        for num in nums:
            if num + diff in seen and num + 2 * diff in seen:
                count += 1
        return count


