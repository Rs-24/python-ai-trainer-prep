# Time to write all of below including tests, explanation and time and aux
# and total space: 13 mins

# Problem: https://leetcode.com/problems/can-place-flowers/description/

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Time: O(n), n = len(flowerbed)
        # Space: O(1)
        total = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                l = (i == 0 or flowerbed[i - 1] == 0)
                r = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if l and r:
                    flowerbed[i] = 1
                    total += 1
        return total >= n

# No mutating in place version:     
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Time: O(n), n = len(flowerbed)
        # Space: O(1)
        total = 0
        prev_planted = False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                prev_planted = True
                continue
            if flowerbed[i] == 0:
                l = (i == 0 or not prev_planted)
                r = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if l and r:
                    total += 1
                    prev_planted = True
                else:
                    prev_planted = False
        return total >= n


