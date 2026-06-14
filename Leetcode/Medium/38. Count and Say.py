

class Solution:
    def countAndSay(self, n: int) -> str:
        # Time: O(n^2)
        # Space: O(n)
        p = "1"
        for _ in range(2, n + 1):
            t = []
            i = 0
            while i < len(p):
                j = i
                while j + 1 < len(p) and p[j] == p[j + 1]:
                    j += 1
                t.append(str(j - i + 1))
                t.append(p[i])
                i += 1
            p = "".join(t)
        return p


