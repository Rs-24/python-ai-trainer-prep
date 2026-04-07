# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/duplicate-zeros/description/

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        n = len(arr)
        zeroes = arr.count(0)
        i = n - 1
        j = n - 1 + zeroes
        while i < j:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1


