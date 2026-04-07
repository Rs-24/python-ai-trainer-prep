# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/shuffle-the-array/description/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        out = []
        for i in range(n):
            out.append(nums[i])
            out.append(nums[i + n])
        return out


