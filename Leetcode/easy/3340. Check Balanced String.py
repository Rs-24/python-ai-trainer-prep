

class Solution:
    def isBalanced(self, num: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        e = o = 0
        for i, d in enumerate(num):
            if i % 2 == 0:
                e += int(d)
            else:
                o += int(d)
        return e == o


