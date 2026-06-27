

class Solution:
    def hIndex(self, citations: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        citations.sort(reverse=True)
        a = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                a = i + 1
            else:
                break
        return a


