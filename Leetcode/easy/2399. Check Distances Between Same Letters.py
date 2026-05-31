

class Solution:
    def checkDistances(self, s: str, distance: list) -> bool:
        # Time: O(n)
        # Space: O(n)
        d = {}
        for i, ch in enumerate(s):
            if ch in d:
                if i - d[ch] - 1 != distance[ord(ch) - ord("a")]:
                    return False
            else:
                d[ch] = i
        return True


