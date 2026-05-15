

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(n)
        c = Counter(arr)
        return len(c.values()) == len(set(c.values()))


