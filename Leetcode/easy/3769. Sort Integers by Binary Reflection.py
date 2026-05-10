# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sort-integers-by-binary-reflection/description/

from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        def reflect(x: int) -> int:
            ref = 0
            while x > 0:
                ref <<= 1
                ref |= (x & 1)
                x >>= 1
            return ref        
        arr = [(reflect(num), num) for num in nums]
        arr.sort()
        return [num for _, num in arr]


