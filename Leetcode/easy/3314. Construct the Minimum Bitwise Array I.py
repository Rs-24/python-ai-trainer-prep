# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        out = []
        for num in nums:
            if num == 2:
                out.append(-1)
                continue
            for i in range(31):
                if ((num >> i) & 1) == 0:
                    out.append(num ^ (1 << i))
                    break
        return out


