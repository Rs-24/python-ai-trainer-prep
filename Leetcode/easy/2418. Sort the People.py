# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sort-the-people/description/

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Time: O(n log n), n = len(names) = len(heights)
        # Space: O(n)
        arr = [(n, h) for n, h in zip(names, heights)]
        arr.sort(key=lambda x: x[1], reverse=True)
        return [n for n, _ in arr]


