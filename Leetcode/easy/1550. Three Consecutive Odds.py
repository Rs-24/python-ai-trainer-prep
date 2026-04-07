# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/three-consecutive-odds/description/

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False


