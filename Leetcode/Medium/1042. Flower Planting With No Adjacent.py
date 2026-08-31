

class Solution:
    def gardenNoAdj(self, n: int, paths: list) -> list:
        # Time: O(m + n)
        # Space: O(m + n)
        t = [[] for _ in range(n)]
        for x, y in paths:
            t[x - 1].append(y - 1)
            t[y - 1].append(x - 1)
        a = [0] * n
        for x in range(n):
            s = set()
            for y in t[x]:
                if a[y] != 0:
                    s.add(a[y])
            for f in range(1, 5):
                if f not in s:
                    a[x] = f
                    break
        return a


