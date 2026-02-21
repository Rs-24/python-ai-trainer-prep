# Time to write all of below including tests, explanation and time and aux 
# space: 9 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/single-number/description/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x

if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([1, 2, 1]) == 2
    assert sol.singleNumber([-1, 0, -1, 0, 9]) == 9

# Explanation: the code XOR's every number together with 0 and outputs the
# result, whereby a ^ a = 0, and 0 ^ a = a
# Time: O(n), n = len(nums)
# Space: O(1)

# Learning lessons (done after completing all of above in 9 mins):
#   - No major learning lessons






