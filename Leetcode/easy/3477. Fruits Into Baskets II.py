# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/fruits-into-baskets-ii/description/

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Time: O(n^2), n = len(fruits)
        # Space: O(n)
        n = len(fruits)
        used = [False] * n
        unplaced = 0
        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced


