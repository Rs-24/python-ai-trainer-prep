

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        m, n = len(s1), len(s2)
        if m > n:
            return False
        t1 = [0] * 26
        t2 = [0] * 26
        for i, ch in enumerate(s1):
            t1[ord(ch) - ord("a")] += 1
            t2[ord(s2[i]) - ord("a")] += 1
        if t1 == t2:
            return True
        for i in range(m, n):
            t2[ord(s2[i]) - ord("a")] += 1
            t2[ord(s2[i - m]) - ord("a")] -= 1
            if t1 == t2:
                return True
        return False


