

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Time: O(n)
        # Space: O(1)
        l, r = 0, int(c ** 0.5)
        while l <= r:
            if l * l + r * r == c:
                return True
            elif l * l + r * r < c:
                l += 1
            else:
                r -= 1
        return False


