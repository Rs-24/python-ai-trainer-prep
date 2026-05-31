

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        w = 0
        for i in range(k):
            w += 1 if blocks[i] == "W" else 0
        best = w
        for i in range(k, len(blocks)):
            w += 1 if blocks[i] == "W" else 0
            w -= 1 if blocks[i - k] == "W" else 0
            best = min(best, w)
        return best


