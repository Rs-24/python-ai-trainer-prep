# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Time: O(n log k + n log n), k = max(arr), n = len(arr)
        # Space: O(n)
        def one_bits(x: int):
            total = 0
            while x > 0:
                x &= (x - 1)
                total += 1
            return total
        nums = []
        for num in arr:
            nums.append((one_bits(num), num))
        nums.sort()
        return [num for _, num in nums]


