# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/description/

from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        left = [float("inf")]
        min_val = nums[0]
        for num in nums[1:]:
            left.append(min_val)
            min_val = min(min_val, num)
        right = [float("inf")]
        min_val = nums[-1]
        for num in nums[:-1][::-1]:
            right.append(min_val)
            min_val = min(min_val, num)
        right.reverse()
        best = float("inf")
        for i, num in enumerate(nums):
            if left[i] < num and right[i] < num:
                best = min(best, left[i] + num + right[i])
        return best if best != float("inf") else -1


