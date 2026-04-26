# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/last-visited-integers/description/

from typing import List
from collections import deque

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = deque()
        ans = []
        minus_ones = 0
        for num in nums:
            if num > 0:
                seen.appendleft(num)
                minus_ones = 0
            else:
                minus_ones += 1
                if minus_ones <= len(seen):
                    ans.append(seen[minus_ones - 1])
                else:
                    ans.append(-1)
        return ans


