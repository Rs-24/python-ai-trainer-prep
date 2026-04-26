# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/ant-on-the-boundary/description/

from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        count = 0
        pos = 0
        for num in nums:
            pos += num
            if pos == 0:
                count += 1
        return count


