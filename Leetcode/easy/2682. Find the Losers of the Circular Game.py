

class Solution:
    def circularGameLosers(self, n: int, k: int) -> list:
        # Time: O(n)
        # Space: O(n)
        s = set()
        i = 0
        step = 1
        while i not in s:
            s.add(i)
            i = (i + step * k) % n
            step += 1
        return [i + 1 for i in range(n) if i not in s]


