# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-k-or-of-an-array/description/

from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        res = 0
        for bit in range(32):
            count = 0
            for num in nums:
                count += (num >> bit) & 1
            res |= (count >= k) << bit
        return res


