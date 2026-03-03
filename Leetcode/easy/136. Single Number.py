# Time to write all of below including tests, explanation and time and aux 
# space: 9 mins

# Problem: https://leetcode.com/problems/single-number/description/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            out ^= num
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([1, 2, 1]) == 2
    assert sol.singleNumber([-1, 0, -1, 0, 9]) == 9

# Explanation: the code uses the XOR operator, where 0 ^ a = a, and a ^ a = 0,
# and performs this operation on every number in nums. At the end, the final
# value of out is the number that only occurs once
# Time: O(n), n = len(nums)
# Space: excluding output: O(1)


