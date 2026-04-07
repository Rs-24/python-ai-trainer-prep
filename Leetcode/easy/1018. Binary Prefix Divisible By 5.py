# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/binary-prefix-divisible-by-5/description/

from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        out = []
        temp = 0
        for num in nums:
            temp <<= 1
            temp |= num
            out.append(temp % 5 == 0)
        return out


