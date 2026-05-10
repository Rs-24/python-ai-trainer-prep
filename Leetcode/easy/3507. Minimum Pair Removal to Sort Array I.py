# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/

from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(1)
        def is_sorted(arr: List[int]) -> bool:
            for i in range(1,len(arr)):
                if arr[i - 1] > arr[i]:
                    return False
            return True
        count = 0
        while not is_sorted(nums):
            min_sum = nums[0] + nums[1]
            idx = 0
            for i in range(1, len(nums) - 1):
                cur_sum = nums[i] + nums[i + 1]
                if cur_sum < min_sum:
                    min_sum = cur_sum
                    idx = i
            nums[idx] = min_sum
            nums.pop(idx + 1)
            count += 1
        return count


