

class Solution:
    def findPeaks(self, mountain: list) -> list:
        # Time: O(n)
        # Space: O(n)
        return [i for i in range(1, len(mountain) - 1) if mountain[i - 1] < mountain[i] > mountain[i + 1]]


