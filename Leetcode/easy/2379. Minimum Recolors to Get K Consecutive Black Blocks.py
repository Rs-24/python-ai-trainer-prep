# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Time: O(n), n = len(blocks)
        # Space: O(1)
        w = 0
        for i in range(k):
            if blocks[i] == "W":
                w += 1
        best = w
        for i in range(k, len(blocks)):
            w += 1 if blocks[i] == "W" else 0
            w -= 1 if blocks[i - k] == "W" else 0
            best = min(best, w)
        return best


