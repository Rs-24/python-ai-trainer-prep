# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/

from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        n = len(arr)
        for i in range(n - n // 4):
            if arr[i] == arr[i + n // 4]:
                return arr[i]


