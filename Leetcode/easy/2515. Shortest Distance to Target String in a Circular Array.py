

class Solution:
    def closestTarget(self, words: list, target: str, startIndex: int) -> int:
        # Time: O(n)
        # Space: O(1)
        b = -1
        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                d = min(d, len(words) - d)
                b = d if b == -1 else min(b, d)
        return b
    

