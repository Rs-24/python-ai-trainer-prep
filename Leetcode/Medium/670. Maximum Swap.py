

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Time: O(n)
        # Space: O(n)
        t = list(str(num))
        d = {}
        for i, x in enumerate(t):
            d[x] = i
        for i, x in enumerate(t):
            for y in range(9, int(x), -1):
                if str(y) in d and d[str(y)] > i:
                    t[i], t[d[str(y)]] = t[d[str(y)]], t[i]
                    return int("".join(t))
        return num


