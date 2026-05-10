

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # Time: O(m * n), m = len(strs), n = len(strs[0])
        # Space: O(1)
        count = 0
        for c in range(len(strs[0])):
            for r in range(1, len(strs)):
                if strs[r - 1][c] > strs[r][c]:
                    count += 1
                    break
        return count


