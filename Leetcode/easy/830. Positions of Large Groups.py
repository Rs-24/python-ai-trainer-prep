

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        # Time: O(n), n = len(s)
        # Space: O(n)
        out = []
        start = end = 0
        for i in range(1, len(s)):
            if i > 0 and s[i] != s[i - 1]:
                end = i - 1
                if end - start + 1 >= 3:
                    out.append([start, end])
                start = end = i
            else:
                end += 1
        if end - start + 1 >= 3:
            out.append([start, end])
        return out


