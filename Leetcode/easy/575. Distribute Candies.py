# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/distribute-candies/description/

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Time: O(n), n = len(candyType)
        # Space, excluding output: O(n)
        return min(len(candyType) // 2, len(set(candyType)))


