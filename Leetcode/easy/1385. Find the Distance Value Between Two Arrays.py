# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Time: O(m * n), m = len(arr1), n = len(arr2)
        # Space: O(1)
        total = 0
        for num1 in arr1:
            all_greater = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    all_greater = False
                    break
            total += 1 if all_greater else 0
        return total


