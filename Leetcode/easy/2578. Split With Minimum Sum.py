

class Solution:
    def splitNum(self, num: int) -> int:
        # Time: O(n log n)
        # Space: O(log n)
        n = sorted(str(num))
        n1, n2 = [], []
        for i, d in enumerate(n):
            if i % 2 == 0:
                n1.append(d)
            else:
                n2.append(d)
        return int("".join(n1)) + int("".join(n2))


