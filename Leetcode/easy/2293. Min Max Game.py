# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/min-max-game/description/

from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Aux space: O(n)
        while len(nums) > 1:
            length = len(nums)
            for i in range(length // 2):
                if i % 2 == 0:
                    nums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    nums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = nums[length:]
        return nums[0]


