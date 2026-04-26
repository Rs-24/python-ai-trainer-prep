# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/

from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2


