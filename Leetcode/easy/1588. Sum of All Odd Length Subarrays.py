# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        n = len(arr)
        total = 0
        for i in range(n):
            num = (i + 1) * (n - i)
            odd_num = (num + 1) // 2
            total += arr[i] * odd_num
        return total


