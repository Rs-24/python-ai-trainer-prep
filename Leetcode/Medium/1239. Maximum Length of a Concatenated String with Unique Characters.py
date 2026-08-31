

class Solution:
    def maxLength(self, arr: list) -> int:
        # Time: O(1)
        # Space: O(1)
        masks = []
        for word in arr:
            mask = 0
            for ch in word:
                bit = 1 << (ord(ch) - ord("a"))
                if mask & bit:
                    mask = 0
                    break
                mask |= bit
            if mask:
                masks.append(mask)
        def dfs(index, used):
            best = used.bit_count()
            for i in range(index, len(masks)):
                if not (used & masks[i]):
                    best = max(best, dfs(i + 1, used | masks[i]))
            return best
        return dfs(0, 0)


