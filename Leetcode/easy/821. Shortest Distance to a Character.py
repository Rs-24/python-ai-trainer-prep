

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        # Time: O(n), n = len(s)
        # Space: O(n)
        n = len(s)
        out = [float("inf")] * n
        last_c = None
        for i, ch in enumerate(s):
            if ch == c:
                last_c = i
                out[i] = 0
            if last_c is not None:
                out[i] = min(out[i], i - last_c)
        last_c = None
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_c = i
                out[i] = 0
            if last_c is not None:
                out[i] = min(out[i], last_c - i)
        return out
  

