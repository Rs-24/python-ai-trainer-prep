# Time to write all of below including tests, why the solution works and time 
# and space complexity: 16 mins

# Problem: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for k in [1, 2]:
                if i + k < len(nums) and nums[i] == nums[i + k]:
                    return nums[i]

if __name__ == "__main__":
    sol = Solution()
    assert sol.repeatedNTimes([1, 2, 3, 3]) == 3
    assert sol.repeatedNTimes([0, 0, 0, 1, 2, 3]) == 0
    assert sol.repeatedNTimes([1, 2, 3, 3, 3, 3, 4, 5]) == 3

# Explanation: the code iterates through nums, and if the number at the
# current index is equal to a number 1 or 2 spaces ahead, then the number at the
# current index is returned
# Time: O(n), n = len(nums)
# Space: O(1)


