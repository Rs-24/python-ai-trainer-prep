# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        min_idx = max_idx = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
            if abs(nums[min_idx] - nums[j]) >= valueDifference:
                return [min_idx, j]
            if abs(nums[max_idx] - nums[j]) >= valueDifference:
                return [max_idx, j]
        return [-1, -1]


