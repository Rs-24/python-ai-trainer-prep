# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Time: O(n), n = len(candies)
        # Space, excluding output: O(1)
        out = []
        best = max(candies)
        for c in candies:
            if c + extraCandies >= best:
                out.append(True)
            else:
                out.append(False)
        return out


