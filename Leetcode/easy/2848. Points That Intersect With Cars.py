# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/points-that-intersect-with-cars/description/

from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Time: O(n), n = total combined ranges in nums
        # Space: O(n)
        window = set()
        for a, b in nums:
            for x in range(a, b + 1):
                window.add(x)
        return len(window)


