# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/house-robber/description/

from typing import List 
from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = prev_prev = 0
        current = 0
        for money in nums:
            current = max(prev, prev_prev + money)
            prev_prev = prev
            prev = current
        return prev

if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1]) == 1
    assert sol.rob([0]) == 0
    assert sol.rob([1, 2, 3]) == 4
    assert sol.rob([1, 0, 3, 5, 2]) == 6

# Explanation: the code iterates through the list while storing the previous
# and previous-previous values and setting the current value to
# current = max(prev, prev_prev + money)
# Time: O(n), n = len(nums)
# Space: O(1)


