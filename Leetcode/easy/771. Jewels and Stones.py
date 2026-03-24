# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/jewels-and-stones/description/

from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Time: O(m + n), m = len(jewels), n = len(stones)
        # Space: O(m + n)
        jewels = Counter(jewels)
        stones = Counter(stones)
        total = 0
        for j in jewels:
            total += stones[j]
        return total

# set() version:
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Time: O(m + n), m = len(jewels), n = len(stones)
        # Space: O(m)
        jewels = set(jewels)
        total = 0
        for s in stones:
            if s in jewels:
                total += 1
        return total


