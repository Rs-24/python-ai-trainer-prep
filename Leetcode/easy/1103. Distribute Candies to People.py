# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/distribute-candies-to-people/description/

from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Time: O(num_people + sqrt(candies))
        # Space, excluding output: O(1)
        out = [0] * num_people
        i = 0
        cur = 1
        while candies > 0:
            out[i] += min(cur, candies)
            candies -= min(cur, candies)
            cur += 1
            i += 1
            if i >= num_people:
                i = 0
        return out


