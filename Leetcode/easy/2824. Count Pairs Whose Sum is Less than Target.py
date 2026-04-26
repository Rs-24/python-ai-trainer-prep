# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] < target:
                count += (r - l)
                l += 1
            else:
                r -= 1
        return count


