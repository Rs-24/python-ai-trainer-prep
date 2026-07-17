

class Solution:
    def maxChunksToSorted(self, arr: list) -> int:
        # Time: O(n)
        # Space: O(1)
        a = t = 0
        for i, x in enumerate(arr):
            t = max(t, x)
            a += t == i
        return a


