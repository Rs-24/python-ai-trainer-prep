# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/valid-mountain-array/description/

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        if len(arr) < 3:
            return False
        top_found = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                if i == len(arr) - 2 or top_found:
                    return False
            elif arr[i] > arr[i + 1]:
                if i == 0:
                    return False
                if not top_found:
                    top_found = True
            else:
                return False
        return True


