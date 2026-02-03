# Time to write all of below including tests, explanation and time and aux
# and total space: 2h 11 mins

# I required help from chatGPT to solve this one 

# Problem: https://leetcode.com/problems/house-robber/description/

from typing import List 
from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev = prev = 0
        for money in nums:
            cur = max(prev, prev_prev + money)
            prev_prev = prev
            prev = cur
        return prev

if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1]) == 1
    assert sol.rob([0]) == 0
    assert sol.rob([1, 2, 3]) == 4
    assert sol.rob([1, 0, 3, 5, 2]) == 6

# Explanation: the code iterates through the list while storing the previous
# and previous-previous values and setting the current value to
# cur = max(prev, prev_prev + money)
# Time: O(n), n = len(nums)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 2h 11 mins):
#   - No major learning lessons




            




