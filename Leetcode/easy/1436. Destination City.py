# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/destination-city/description/

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Time: O(n), n = len(paths)
        # Space: O(n)
        cities = set()
        for a, _ in paths:
            cities.add(a)
        for _, b in paths:
            if b not in cities:
                return b


