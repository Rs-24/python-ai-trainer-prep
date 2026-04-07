# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Time: O(n log n), n = len(arr)
        # Space: O(n)
        arr.sort()
        prev = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != prev:
                return False
        return True


