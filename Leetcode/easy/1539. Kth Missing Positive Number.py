# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/kth-missing-positive-number/description/

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Time: O(log n), n = len(arr)
        # Space: O(1)
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k


