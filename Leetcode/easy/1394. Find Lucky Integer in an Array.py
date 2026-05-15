

from collections import Counter

class Solution:
    def findLucky(self, arr: list) -> int:
        # Time: O(n), n = len(arr)
        # Space: O(n)
        c = Counter(arr)
        best = -1
        for num, freq in c.items():
            if num == freq:
                best = max(best, num)
        return best 


